import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker , declarative_base

DATABASE_URL = os.environ['DATABASE_URL']

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Video(Base) :
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    caption = Column(String)
    url_240p = Column(String)
    url_480p = Column(String)
    url_720p = Column(String)

