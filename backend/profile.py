from enum import Enum
from uuid import UUID
from sqlalchemy import select
from database import Database, User


class ProfileBackend:
    class Status(Enum):
        Online = 'Online'
        Away = 'Away'
        DoNotDisturb = 'Do Not Disturb'
        Offline = 'Invisible'

    class Profile:
        def __init__(self, user):
            self.uuid: UUID = user.uuid
            self.username: str = user.username

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
            profile = ProfileBackend.Profile(user)
            session.commit()
        return profile
