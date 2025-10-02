from typing import TYPE_CHECKING, cast, Union, Optional
from uuid import UUID
from sqlalchemy import select, func

from PySide6.QtCore import Signal
from PySide6.QtGui import QImage, QPixmap
from sqlalchemy.orm import aliased

from .base import BaseBackend
from .multithreading import multithreaded
from .cached_object import CachedObject
from .storage import StorageBackend
from database import (
    Database, Server, ServerSortOrder, ServerMember,
    User, Role, ChatCategory, Chat
)

if TYPE_CHECKING:
    from .chat import ChatBackend
    from .profile import ProfileBackend


class ServerBackend(BaseBackend):
    class Server(CachedObject):
        selected_chat_changed = Signal()

        def __init__(self, server, **kwargs):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.__uuid)
            self.__selected_chat: Optional['ChatBackend.Chat'] = None
            self.__selected_chat_uuid: UUID = server.selected_chat_uuid
            self.__members: list['ProfileBackend.Profile'] | None = None

        def update(self, server, **kwargs):
            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.__uuid)
            self.__selected_chat: Optional['ChatBackend.Chat'] = None
            self.__selected_chat_uuid: UUID = server.selected_chat_uuid
            self.changed.emit()

        def update_selected_chat(self, profile_uuid: UUID):
            backend = BaseBackend.get_backend('ChatBackend')
            if TYPE_CHECKING:
                backend = cast(ChatBackend, backend)
            chat = backend.get_chat(profile_uuid, self.__selected_chat_uuid)
            if chat is None:
                chat = backend.get_first_chat(profile_uuid, self.__uuid)
                ServerBackend.edit_server(self.__uuid, selected_chat_uuid=chat.uuid)
            if self.__selected_chat == chat:
                return
            self.__selected_chat: 'ChatBackend.Chat' = chat
            self.selected_chat_changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def icon(self): return self.__icon
        @property
        def selected_chat(self): return self.__selected_chat

        @property
        def members(self):
            if self.__members is None:
                self.load_members()
            return self.__members.copy()

        def load_members(self):
            self.__members = ServerBackend.get_server_members(self.__uuid)

        @name.setter
        def name(self, new_value: str):
            self.__name = new_value
            ServerBackend.edit_server(self.__uuid, name=new_value)
            self.changed.emit()

        @icon.setter
        def icon(self, new_value: Union[QImage, QPixmap]):
            if isinstance(new_value, QPixmap):
                new_value = new_value.toImage()
            self.__icon = new_value
            StorageBackend.Server.set_icon(self.__uuid, new_value)
            self.changed.emit()

        @selected_chat.setter
        def selected_chat(self, new_value: 'ChatBackend.Chat'):
            if self.__selected_chat == new_value:
                return
            self.__selected_chat = new_value
            self.__selected_chat_uuid = new_value.uuid
            ServerBackend.edit_server(self.__uuid, selected_chat_uuid=new_value.uuid)
            self.selected_chat_changed.emit()

    @staticmethod
    def get_server_members(server_uuid: UUID):
        with Database.create_session() as session:
            top_roles = (
                select(User.uuid.label('user_uuid'), Role)
                .join(Role, User.roles)
                .where(Role.server_uuid == server_uuid)
                .where(Role.public)
                .group_by(User)
                .having(Role.sort_order == func.min(Role.sort_order))
                .subquery()
            )
            TopRole = aliased(Role, top_roles)
            # noinspection PyUnresolvedReferences
            top_role_order = TopRole.sort_order.desc()

            result = session.execute(
                select(User, TopRole)
                .outerjoin(top_roles, User.uuid == top_roles.c.user_uuid)
                .join(ServerMember, User.member_of)
                .where(ServerMember.server_uuid == server_uuid)
                .order_by(top_role_order, User.username.desc(), User.uuid)
            ).all()

            backend = BaseBackend.get_backend('ProfileBackend')
            if TYPE_CHECKING:
                backend = cast(ProfileBackend, backend)
            members = [backend.Profile(_member, top_role=top_role) for _member, top_role in result]
        return members

    @staticmethod
    def get_server(profile_uuid: UUID, server_uuid):
        if not isinstance(server_uuid, UUID):
            try:
                server_uuid = UUID(str(server_uuid))
            except ValueError:
                return None
        with Database.create_session() as session:
            _server = session.scalars(
                select(Server)
                .where(Server.uuid == server_uuid)
                .where(Server.members.any(ServerMember.user_uuid == profile_uuid))
            ).one_or_none()
            if _server is None:
                return None
            server = ServerBackend.Server(_server)
            server.update_selected_chat(profile_uuid)
        return server

    @staticmethod
    def get_saved_messages(profile_uuid: UUID):
        with Database.create_session() as session:
            _server = session.scalar(
                select(Server)
                .join(
                    ServerSortOrder,
                    (Server.uuid == ServerSortOrder.server_uuid)
                    & (ServerSortOrder.user_uuid == profile_uuid)
                )
                .where(ServerSortOrder.sort_order == 1)
            )
            server = ServerBackend.Server(_server)
            server.update_selected_chat(profile_uuid)
        return server

    @staticmethod
    def get_server_list_pinned(profile_uuid: UUID):
        with Database.create_session() as session:
            servers = session.scalars(
                select(Server)
                .join(
                    ServerSortOrder,
                    (Server.uuid == ServerSortOrder.server_uuid)
                    & (ServerSortOrder.user_uuid == profile_uuid)
                )
                .where(ServerSortOrder.sort_order > 0)
                .order_by(ServerSortOrder.sort_order)
            ).all()
            server_list = [ServerBackend.Server(server) for server in servers]
            for server in server_list:
                server.update_selected_chat(profile_uuid)
        return server_list

    @staticmethod
    def get_server_list_unpinned(profile_uuid: UUID):
        with Database.create_session() as session:
            servers = session.scalars(
                select(Server)
                .join(
                    ServerSortOrder,
                    (Server.uuid == ServerSortOrder.server_uuid)
                    & (ServerSortOrder.user_uuid == profile_uuid)
                )
                .where(ServerSortOrder.sort_order == 0)
                .order_by(Server.created_at)
            ).all()
            server_list = [ServerBackend.Server(server) for server in servers]
            for server in server_list:
                server.update_selected_chat(profile_uuid)
        return server_list

    @staticmethod
    @multithreaded
    def edit_server(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            server = session.get(Server, uuid)
            for kw, value in kwargs.items():
                setattr(server, kw, value)
            session.add(server)
            session.commit()

    @staticmethod
    @multithreaded
    def reorder_server(profile_uuid: UUID, server_uuid: UUID, new_order: int):
        with Database.create_session() as session:
            server_sort_order = session.get(ServerSortOrder, {'server_uuid': server_uuid, 'user_uuid': profile_uuid})
            server_sort_order.sort_order = new_order
            session.add(server_sort_order)
            session.commit()

    @staticmethod
    @multithreaded
    def reorder_server_list(profile_uuid: UUID, new_order: list[UUID]):
        with Database.create_session() as session:
            server_sort_orders = session.scalars(
                select(ServerSortOrder)
                .where(ServerSortOrder.user_uuid == profile_uuid)
            ).all()
            server_sort_map = {server_sort.server_uuid: server_sort for server_sort in server_sort_orders}
            for i, uuid in enumerate(new_order, start=1):
                server_sort_map.pop(uuid).sort_order = i
            for server_sort in server_sort_map.values():
                server_sort.sort_order = 0
            session.add_all(server_sort_orders)
            session.commit()

    @staticmethod
    def create_server(name: str, profile_uuid: UUID, sort_order=0):
        with Database.create_session() as session:
            _server = Server(name=name)
            session.add(_server)
            session.flush()
            session.refresh(_server)
            server_sort_order = ServerSortOrder(
                server_uuid=_server.uuid,
                user_uuid=profile_uuid,
                sort_order=sort_order
            )

            profile = session.get(User, profile_uuid)
            server_member = ServerMember(server=_server, user=profile)
            owner_role = Role(
                name='Owner', color=0xFFFFC814, pingable=True,
                server=_server, users=[profile], sort_order=0
            )
            everyone_role = Role(
                name='Everyone', color=0xFF808080, public=False, pingable=True,
                server=_server, users=[profile], sort_order=1
            )

            category = ChatCategory(
                name='Text Chats', server=_server,
                sort_order=1, whitelisted_roles=[owner_role, everyone_role]
            )
            chat = Chat(
                name='General', category=category,
                sort_order=1, whitelisted_roles=[owner_role, everyone_role]
            )

            session.add_all([
                server_sort_order, profile, server_member,
                owner_role, everyone_role, category, chat
            ])
            session.commit()
            server = ServerBackend.Server(_server)
            server.update_selected_chat(profile_uuid)
        return server
