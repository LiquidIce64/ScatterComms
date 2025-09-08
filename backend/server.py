from typing import Union
from uuid import UUID
from sqlalchemy import select

from PySide6.QtGui import QImage, QPixmap

from database.models import ServerSortOrder
from .multithreading import multithreaded
from .storage import StorageBackend
from .cached_object import CachedObject
from database import Database, Server, ServerMember, User, Role


class ServerBackend:
    class Server(CachedObject):
        def __init__(self, server):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.uuid)
            self._initialized = True

        def update(self, server):
            self.__uuid: UUID = server.uuid
            self.__name: str = server.name
            self.__icon = StorageBackend.Server.get_icon(self.uuid)
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def icon(self): return self.__icon

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
                name='Owner', color=0xFFC814FF,
                server=_server, users=[profile], sort_order=0
            )
            session.add_all([server_sort_order, profile, server_member, owner_role])
            session.commit()
            server = ServerBackend.Server(_server)
        return server
