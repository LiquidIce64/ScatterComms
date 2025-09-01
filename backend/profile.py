from typing import Optional
from sqlalchemy import select
from database import SessionMaker, User


class ProfileBackend:
    class Profile:
        def __init__(self, user):
            self.username: str = user.username
            self.avatar_path: Optional[str] = user.avatar_path

    @staticmethod
    def get_profiles():
        with SessionMaker() as session:
            users = session.scalars(
                select(User)
                .where(User.owned_by_me == True)
                .order_by(User.created_at)
            ).all()
            profiles = [ProfileBackend.Profile(user) for user in users]
        return profiles

    @staticmethod
    def create_profile(username: str):
        with SessionMaker() as session:
            user = User(username=username, owned_by_me=True)
            session.add(user)
            profile = ProfileBackend.Profile(user)
            session.commit()
        return profile
