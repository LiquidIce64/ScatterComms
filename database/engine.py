from typing import Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from .models import *

engine: Optional[Engine] = None

SessionMaker: Optional[sessionmaker] = None


def init_database(filepath: str):
    global engine
    global SessionMaker
    engine = create_engine('sqlite:///' + filepath)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(engine)
