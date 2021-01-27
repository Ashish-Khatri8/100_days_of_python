# Day 34 project - The Quizzler App.

# Import required modules.
from tkinter import *
from html import unescape
from question_bank import QuestionBank


class Quizzler:
    """A class to represent the Quizzler app."""
    def __init__(self):
        """Initialize app attributes and methods."""
        self.questions = QuestionBank().questions
        self.correct_answer = None
        self.question_no = 0
        self.score = 0
        self._create_ui()
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        """Displays next question on canvas."""
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.canvas_text, fill=self.color)
        if self.question_no < 10:
            new_question = self.questions[self.question_no]
            for question, answer in new_question.items():
                self.canvas.itemconfig(
                    self.canvas_text,
                    text=f"{self.question_no+1}. {unescape(question)}"
                )
                self.correct_answer = answer
                self.question_no += 1
        else:
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"
            self.canvas.itemconfig(
                self.canvas_text,
                text=f"Your final score : {self.score}/10")

    def true_button_clicked(self):
        """Sets user_answer to True and then checks the answer."""
        user_answer = "True"
        self.check_answer(user_answer)

    def false_button_clicked(self):
        """Sets user_answer to False and then checks the answer."""
        user_answer = "False"
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        """Checks user's answer against correct answer."""
        if user_answer == self.correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score : {self.score}")
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_text, fill="white")
        self.window.after(1500, self.next_question)

    def _create_ui(self):
        """Creates the user interface of the app."""
        self.color = "cadet blue"
        self.font = ("Arial", 20, "bold", "italic")
        self._create_window()
        self._create_canvas()
        self._create_buttons()

    def _create_window(self):
        """Creates the app window,"""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=self.color)
        # Score label.
        self.score_label = Label(text=f"Score : {self.score}")
        self.score_label.grid(row=0, column=1)
        self.score_label.config(bg=self.color, font=self.font, fg="white smoke")

    def _create_canvas(self):
        """Creates the window canvas."""
        self.canvas = Canvas(width=400, height=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.canvas_text = self.canvas.create_text(
            200, 150, fill=self.color, text="Hello",
            font=self.font, width=380
        )

    def _create_buttons(self):
        """Creates the app buttons."""
        # True button.
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(command=self.true_button_clicked)
        # False button.
        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(command=self.false_button_clicked)


# Create a class object to start the quiz.
quiz = Quizzler()
