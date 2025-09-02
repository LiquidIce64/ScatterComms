from sqlalchemy import select
from database import Database, User


class ProfileBackend:
    class Profile:
        def __init__(self, user):
            self.username: str = user.username
            self.load_avatar: bool = user.load_avatar

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
    def create_profile(username: str):
        with Database.create_session() as session:
            user = User(username=username, owned_by_me=True)
            session.add(user)
            profile = ProfileBackend.Profile(user)
            session.commit()
        return profile
