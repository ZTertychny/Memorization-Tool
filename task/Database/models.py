from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = "flashcard"
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    answer = Column(String)
    box_num = Column(Integer)
