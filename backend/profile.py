from typing import Union
from enum import Enum
from uuid import UUID
from sqlalchemy import select

from PySide6.QtGui import QImage, QPixmap

from .cached_object import CachedObject
from .multithreading import multithreaded
from .storage import StorageBackend
from .server import ServerBackend
from database import Database, User


class ProfileBackend:
    class Status(Enum):
        Online = 'Online'
        Away = 'Away'
        DoNotDisturb = 'Do Not Disturb'
        Offline = 'Invisible'

    class Profile(CachedObject):
        def __init__(self, user):
            if hasattr(self, '_initialized'):
                return
            super().__init__()
            self.__uuid: UUID = user.uuid
            self.__username: str = user.username
            self.__avatar = StorageBackend.Profile.get_avatar(self.uuid)
            self._initialized = True

        def update(self, user):
            self.__uuid: UUID = user.uuid
            self.__username: str = user.username
            self.__avatar = StorageBackend.Profile.get_avatar(self.uuid)
            self.changed.emit()

        @property
        def uuid(self): return self.__uuid
        @property
        def username(self): return self.__username
        @property
        def avatar(self): return self.__avatar

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

    @staticmethod
    def get_profiles():
        with Database.create_session() as session:
            users = session.scalars(
                select(User)
                .where(User.owned_by_me == True)
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
                .where(User.owned_by_me == True)
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
            ServerBackend.create_server('Saved Messages', profile.uuid, sort_order=1)
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
