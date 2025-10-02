from typing import TYPE_CHECKING, cast
from uuid import UUID
from sqlalchemy import select, func

from PySide6.QtGui import QColor

from .base import BaseBackend
from .multithreading import multithreaded
from .cached_object import CachedObject
from database import Database, User, Role, chat_roles, ChatCategory, Chat

if TYPE_CHECKING:
    from .profile import ProfileBackend


class RoleBackend(BaseBackend):
    class Role(CachedObject):
        def __init__(self, role):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = role.uuid
            self.__name: str = role.name
            self.__color = QColor.fromRgba(role.color)
            self.__public: bool = role.public
            self.__pingable: bool = role.pingable

        def update(self, role):
            self.__uuid: UUID = role.uuid
            self.__name: str = role.name
            self.__color = QColor.fromRgba(role.color)
            self.__public: bool = role.public
            self.__pingable: bool = role.pingable
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def name(self): return self.__name
        @property
        def color(self): return self.__color
        @property
        def public(self): return self.__public
        @property
        def pingable(self): return self.__pingable

        def save_changes(self, name: str, color: QColor, public: bool, pingable: bool):
            self.__name: str = name
            self.__color = color
            self.__public: bool = public
            self.__pingable: bool = pingable
            RoleBackend.edit_role(
                self.__uuid,
                name=name, color=color.rgba(),
                public=public, pingable=pingable
            )
            self.changed.emit()

    @staticmethod
    def get_top_role(profile_uuid: UUID, server_uuid: UUID):
        with Database.create_session() as session:
            _role = session.scalars(
                select(Role)
                .join(User, Role.users)
                .where(Role.public)
                .where(User.uuid == profile_uuid)
                .where(Role.server_uuid == server_uuid)
                .order_by(Role.sort_order)
            ).first()
            if _role is None:
                return None
            role = RoleBackend.Role(_role)
        return role

    @staticmethod
    def get_whitelisted_roles(chat_uuid: UUID):
        with Database.create_session() as session:
            # noinspection PyTypeChecker
            roles = session.scalars(
                select(Role)
                .join(chat_roles, (
                    (chat_roles.c.role_uuid == Role.uuid)
                    & (chat_roles.c.chat_uuid == chat_uuid)
                ))
            ).all()
            role_list = [RoleBackend.Role(role) for role in roles]
        return role_list

    @staticmethod
    def get_chat_members(chat_uuid: UUID):
        with Database.create_session() as session:
            user_whitelisted = User.roles.any(Role.uuid.in_(
                select(Role.uuid)
                .join_from(ChatCategory, Role, ChatCategory.whitelisted_roles)
                .join(Chat)
                .where(Chat.uuid == chat_uuid)
                .intersect(
                    select(Role.uuid)
                    .join_from(Chat, Role, Chat.whitelisted_roles)
                    .where(Chat.uuid == chat_uuid)
                )
            ))

            # Get grouped roles and their members
            result = session.execute(
                select(User, Role)
                .join(Role, User.roles)
                .where(Role.public & Role.grouped)
                .where(Role.server_uuid == (
                    select(ChatCategory.server_uuid)
                    .join(Chat)
                    .where(Chat.uuid == chat_uuid)
                    .scalar_subquery()
                ))
                .where(user_whitelisted)
                .group_by(User)
                .having(Role.sort_order == func.min(Role.sort_order))
                .order_by(Role.sort_order, User.username, User.uuid)
            ).all()

            # Turn that into backend objects
            backend = BaseBackend.get_backend('ProfileBackend')
            if TYPE_CHECKING:
                backend = cast(ProfileBackend, backend)
            member_uuids: list[UUID] = []
            grouped_roles: list[tuple[RoleBackend.Role, list[backend.Profile]]] = []
            last_role = None
            for _member, role in result:
                member_uuids.append(_member.uuid)
                member = backend.Profile(_member)
                if role != last_role:
                    last_role = role
                    grouped_roles.append((RoleBackend.Role(role), [member]))
                else:
                    grouped_roles[-1][1].append(member)

            # Get everyone else
            _ungrouped = session.scalars(
                select(User)
                .where(User.uuid.not_in(member_uuids))
                .where(user_whitelisted)
            ).all()
            ungrouped = [backend.Profile(_member) for _member in _ungrouped]
        return grouped_roles, ungrouped

    @staticmethod
    @multithreaded
    def edit_role(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            role = session.get(Role, uuid)
            for kw, value in kwargs.items():
                setattr(role, kw, value)
            session.add(role)
            session.commit()

    @staticmethod
    def create_role(server_uuid: UUID, name: str):
        with Database.create_session() as session:
            sort_order = session.scalar(
                select(func.max(Role.sort_order))
                .where(Role.server_uuid == server_uuid)
            )
            everyone_role = session.scalar(
                select(Role)
                .where(Role.server_uuid == server_uuid)
                .where(Role.sort_order == sort_order)
            )
            everyone_role.sort_order += 1
            _role = Role(
                server_uuid=server_uuid,
                name=name, color=0xFF808080,
                sort_order=sort_order, public=True
            )
            session.add(everyone_role, _role)
            session.commit()
            role = RoleBackend.Role(_role)
        return role
