from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)

    def create_flashcard(self, data):
        session = self.maker()
        flashcard = models.Flashcard(**data)
        session.add(flashcard)
        session.commit()

    def get_flashcard(self):
        session = self.maker()
        flashcards_list = session.query(models.Flashcard).all()
        return flashcards_list

    def update_flashcard(self, filter_data, data):
        session = self.maker()
        upt_query = session.query(models.Flashcard).filter(models.Flashcard.id == filter_data)
        if len(data) == 1:
            if data.get("question"):
                upt_query.update({models.Flashcard.question: data["question"]})
            elif data.get("answer"):
                upt_query.update({models.Flashcard.answer: data["answer"]})
            elif data.get("box_num"):
                upt_query.update({models.Flashcard.box_num: data["box_num"]})
        else:
            upt_query.update({models.Flashcard.question: data["question"],
                              models.Flashcard.answer: data["answer"]})
        session.commit()

    def delete_flashcard(self, filter_data):
        session = self.maker()
        session.query(models.Flashcard).filter(models.Flashcard.id == filter_data).delete(synchronize_session=False)
        session.commit()
