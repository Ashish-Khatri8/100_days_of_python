# Day 17 project - Quiz game.

# Import required modules.
from question_model import Question
from data import quiz_data, logo
from quiz_brain import QuizBrain
from random import randint

# List to store questions for quiz.
question_bank = []

# List to store randomly generated numbers.
random_nums = []

# Model 10 random questions for quiz and add them to the question bank.
while len(question_bank) < 10:
    no = randint(0, 49)
    # Check if the same no has not been generated before already,
    # As it will make the same question to be added twice to the question_bank.
    if no not in random_nums:
        # Add no to random_nums.
        random_nums.append(no)
        new_question = quiz_data[no]["question"]
        new_answer = quiz_data[no]["answer"]
        # Model the question and add it to question bank.
        question = Question(new_question, new_answer)
        question_bank.append(question)
        
# Print quiz logo.
print(logo)

# Create an object of class QuizBrain with question_bank as argument.
quiz = QuizBrain(question_bank)

# Check if all questions have been asked, if not ask the next question.
while quiz.still_has_questions():
    quiz.next_question()

# Display user's final score.
print("\nYou completed the quiz!")
print(f"Your final score : {quiz.score}/{quiz.question_number}.\n")
