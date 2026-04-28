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
    url_480p = Column(String)
    url_720p = Column(String)



def upload_video(title , caption , url_480p , url_720p ):
    db = sessionLocal()
    video = Video(title , caption , url_480p , url_720p)
    db.add(video)
    db.commit()


def delete_video():
    pass

def get_video():
    pass




