from typing import Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from .models import Base


class Database:
    engine: Optional[Engine] = None
    SessionMaker: Optional[sessionmaker] = None

    @classmethod
    def init(cls, filepath: str):
        cls.engine = create_engine('sqlite:///' + filepath)
        Base.metadata.create_all(cls.engine)
        cls.SessionMaker = sessionmaker(cls.engine)

    @classmethod
    def create_session(cls):
        return cls.SessionMaker()
