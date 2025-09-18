from uuid import UUID
from sqlalchemy import select, func

from PySide6.QtGui import QColor

from .multithreading import multithreaded
from .cached_object import CachedObject
from .profile import ProfileBackend
from database import Database, Chat, ChatCategory, User, Role


def select_whitelisted_roles(chat_uuid: UUID):
    return (
        select(Chat.whitelisted_roles.concat(ChatCategory.whitelisted_roles).distinct())
        .join(ChatCategory, ChatCategory.uuid == Chat.category_uuid)
        .where(Chat.uuid == chat_uuid)
    )


class RoleBackend:
    class Role(CachedObject):
        def __init__(self, role):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self.__uuid: UUID = role.uuid
            self.__name: str = role.name
            self.__color = QColor.fromRgba(role.color)
            self.__public: bool = role.public
            self.__pingable: bool = role.pingable
            self._initialized = True

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
    def get_whitelisted_roles(chat_uuid: UUID):
        with Database.create_session() as session:
            roles = session.scalars(select_whitelisted_roles(chat_uuid)).all()
            role_list = [ProfileBackend.Profile(role) for role in roles]
        return role_list

    @staticmethod
    def get_chat_members(chat_uuid: UUID):
        with Database.create_session() as session:
            members = session.scalars(
                select(User)
                .where(User.roles.in_(select_whitelisted_roles(chat_uuid)))
            ).all()
            member_list = [ProfileBackend.Profile(member) for member in members]
        return member_list

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
                name=name, color=0x808080FF,
                sort_order=sort_order
            )
            session.add(everyone_role, _role)
            session.commit()
            role = RoleBackend.Role(_role)
        return role
