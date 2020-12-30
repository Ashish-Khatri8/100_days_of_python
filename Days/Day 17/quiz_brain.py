class QuizBrain:

    def __init__(self, question_list):
        """
        Initializes question_list, score and question_number.
        """
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """
        Prompts user for answer and checks it.
        """
        choice = input(f"Q{self.question_number+1}: {self.question_list[self.question_number].text}?"
                       f"\nTrue or False :\t")
        self.check_answer(choice)
        self.question_number += 1

    def still_has_questions(self):
        """
        Returns False if there are no more questions to be asked, otherwise True.
        """
        if self.question_number == len(self.question_list):
            return False
        return True

    def check_answer(self, choice):
        """
        Checks if the user's answer was right and increments the score.
        """
        if choice == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
            print(f"The right answer was {self.question_list[self.question_number].answer}.")
        print(f"Your current score : {self.score}/{self.question_number+1}\n")
