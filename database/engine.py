from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import *

engine = create_engine("sqlite:///test.db")

Base.metadata.create_all(engine)

SessionMaker = sessionmaker(engine)
