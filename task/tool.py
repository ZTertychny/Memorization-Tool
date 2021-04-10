from Database.db import Database


class FlashCards:

    def __init__(self, database):
        self.flashcards = dict()
        self.db = database

    def flashcards_action(self):
        while True:
            flashcards_act = input("\n1. Add a new flashcard\n2. Exit\n")
            if flashcards_act == "1" or flashcards_act == "2":
                while flashcards_act != "2":
                    question = input("Question:\n")
                    while not question:
                        question = input("Question:\n")
                    answer = input("Answer:\n")
                    while not answer:
                        answer = input("Answer:\n")
                    self.db.create_flashcard({"question": question, "answer": answer})
                    break
                else:
                    print()
                    break
            else:
                print(f"\n{flashcards_act} is not an option\n")

    def practice_flashcards(self):
        flashcards = self.db.get_flashcard()
        if flashcards:
            for card in flashcards:
                print(f"\nQuestion: {card.question}")
                act = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n')
                if act == "y":
                    print(f"\nAnswer: {card.answer}\n")
                elif act == "u":
                    # self.edit_flashcard(card)
                    upt_act = input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')
                    if upt_act == "e":
                        new_ques = input(f"\ncurrent question: {card.question}\nplease write a new question:\n")
                        new_ans = input(f"\ncurrent answer: {card.answer}\nplease write a new answer:\n")
                        self.db.update_flashcard(card.id, {"question": new_ques, "answer": new_ans})
                    elif upt_act == "d":
                        self.db.delete_flashcard(card.id)
                    else:
                        print(f"\n{upt_act} is not an option\n")
                else:
                    continue
                print()
        else:
            print("\nThere is no flashcard to practice!\n")

    # def edit_flashcard(self, card):
    #     upt_act = input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')
    #     if upt_act == "e":
    #         new_ques = input(f"\ncurrent question: {card.question}\nplease write a new question:\n")
    #         new_ans = input(f"\ncurrent answer: {card.answer}\nplease write a new answer:\n")
    #         self.db.update_flashcard(card.id, {"question": new_ques, "answer": new_ans})
    #     elif upt_act == "d":
    #         self.db.delete_flashcard(card.id)
    #     else:
    #         print(f"\n{upt_act} is not an option\n")

    def main(self):
        while True:
            ext_choice = input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")
            if ext_choice == "1":
                self.flashcards_action()
            elif ext_choice == "2":
                self.practice_flashcards()
            elif ext_choice == "3":
                return f"\nBye!"
            else:
                print(f"\n{ext_choice} is not an option\n")


if __name__ == '__main__':
    db = Database("sqlite:///flashcard.db")
    start = FlashCards(db)
    print(start.main())
