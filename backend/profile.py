from typing import TYPE_CHECKING, cast, Union, Optional
from enum import Enum
from uuid import UUID
from sqlalchemy import select

from PySide6.QtCore import Signal
from PySide6.QtGui import QImage, QPixmap

from .base import BaseBackend
from .cached_object import CachedObject
from .multithreading import multithreaded
from .storage import StorageBackend
from database import Database, User

if TYPE_CHECKING:
    from .server import ServerBackend
    from .role import RoleBackend


class ProfileBackend(BaseBackend):
    class Status(Enum):
        Online = 'Online'
        Away = 'Away'
        DoNotDisturb = 'Do Not Disturb'
        Offline = 'Invisible'

    class Profile(CachedObject):
        top_role_changed = Signal()

        def __init__(self, user, **kwargs):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self._initialized = True

            self.__uuid: UUID = user.uuid
            self.__username: str = user.username
            self.__avatar = StorageBackend.Profile.get_avatar(self.uuid)

            self.__top_role: Optional['RoleBackend.Role'] = None
            top_role = kwargs.get('top_role', None)
            if top_role is not None:
                role_backend = BaseBackend.get_backend('RoleBackend')
                if TYPE_CHECKING:
                    role_backend = cast(RoleBackend, role_backend)
                self.__top_role = role_backend.Role(top_role)

        def update(self, user, **kwargs):
            self.__uuid: UUID = user.uuid
            self.__username: str = user.username
            self.__avatar = StorageBackend.Profile.get_avatar(self.uuid)
            top_role = kwargs.get('top_role', -1)
            if top_role is None:
                self.top_role = None
            elif top_role != -1:
                role_backend = BaseBackend.get_backend('RoleBackend')
                if TYPE_CHECKING:
                    role_backend = cast(RoleBackend, role_backend)
                self.top_role = role_backend.Role(top_role)
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def username(self): return self.__username
        @property
        def avatar(self): return self.__avatar
        @property
        def top_role(self): return self.__top_role

        @username.setter
        def username(self, new_value: str):
            self.__username = new_value
            ProfileBackend.edit_user(self.__uuid, username=new_value)
            self.changed.emit()

        @avatar.setter
        def avatar(self, new_value: Union[QImage, QPixmap]):
            if isinstance(new_value, QPixmap):
                new_value = new_value.toImage()
            self.__avatar = new_value
            StorageBackend.Profile.set_avatar(self.__uuid, new_value)
            self.changed.emit()

        @top_role.setter
        def top_role(self, new_value: 'RoleBackend.Role'):
            if self.__top_role == new_value:
                return
            self.__top_role = new_value
            self.top_role_changed.emit()

    @staticmethod
    def get_profiles():
        with Database.create_session() as session:
            users = session.scalars(
                select(User)
                .where(User.owned_by_me)
                .order_by(User.created_at)
            ).all()
            profiles = [ProfileBackend.Profile(user) for user in users]
        return profiles

    @staticmethod
    def get_profile(uuid):
        if not isinstance(uuid, UUID):
            try:
                uuid = UUID(str(uuid))
            except ValueError:
                return None
        with Database.create_session() as session:
            user = session.scalars(
                select(User)
                .where(User.uuid == uuid)
                .where(User.owned_by_me)
            ).one_or_none()
            if user is None:
                return None
            profile = ProfileBackend.Profile(user)
        return profile

    @staticmethod
    def create_profile(username: str):
        with Database.create_session() as session:
            user = User(username=username, owned_by_me=True)
            session.add(user)
            session.commit()
            profile = ProfileBackend.Profile(user)

            server_backend = BaseBackend.get_backend('ServerBackend')
            if TYPE_CHECKING:
                server_backend = cast(ServerBackend, server_backend)
            server_backend.create_server('Saved Messages', profile.uuid, sort_order=1)
        return profile

    @staticmethod
    @multithreaded
    def edit_user(uuid: UUID, **kwargs):
        with Database.create_session() as session:
            user = session.get(User, uuid)
            for kw, value in kwargs.items():
                setattr(user, kw, value)
            session.add(user)
            session.commit()
