import requests


class QuestionBank:
    """A class to create the question bank from the OpenTrivia API."""
    def __init__(self):
        """Initialize the question bank."""
        self.questions = []
        self._create_question_bank()

    def _create_question_bank(self):
        """Gets data from API and creates the question bank."""
        parameters = {
            "amount": 10,
            "type": "boolean",
        }
        response = requests.get(
            url="https://opentdb.com/api.php",
            params=parameters
        )
        data = response.json()["results"]
        for each_question in data:
            new_question = {}
            question = each_question["question"]
            answer = each_question["correct_answer"]
            new_question[question] = answer
            self.questions.append(new_question)
