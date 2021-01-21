# Day 31 project - Flash Card GUI App.

# Import required modules.
from tkinter import *
from random import choice
import pandas


class FlashCard:
    """A class to represent the Flash Card App."""
    def __init__(self):
        """Initialize app attributes and methods."""
        self.bg_color = "#B1DDC6"
        self._create_user_interface()
        self._read_data()
        self.window.mainloop()

    def _read_data(self):
        """Reads data from the csv file."""
        try:
            self.data = pandas.read_csv("./data/words_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("./data/french_words.csv")
        finally:
            self.words_data = self.data.to_dict(orient="records")
            self.new_card()

    def new_card(self):
        """Gets a new random pair and shows the french word on canvas."""
        self.window.after_cancel(self.flip_timer)
        self.new_pair = choice(self.words_data)
        self.canvas.itemconfig(self.language_text, text="French", fill="black")
        self.canvas.itemconfig(self.word_text, text=self.new_pair["French"], fill="black")
        self.canvas.itemconfig(self.canvas_image, image=self.front_image)
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        """Flips the card and shows the english meaning of french word."""
        self.canvas.itemconfig(self.canvas_image, image=self.back_image)
        self.canvas.itemconfig(self.language_text, text="English", fill="white")
        self.canvas.itemconfig(self.word_text, text=self.new_pair["English"], fill="white")

    def is_known(self):
        """Removes the word whose meaning user knows from the words_to_learn.csv file."""
        self.words_data.remove(self.new_pair)
        data = pandas.DataFrame(self.words_data)
        data.to_csv("./data/words_to_learn.csv", index=False)
        self.new_card()

    def _create_user_interface(self):
        """Creates the complete user interface for the app."""
        self._create_window()
        self._create_canvas()
        self._create_buttons()

    def _create_window(self):
        """Creates the app window."""
        self.window = Tk()
        self.window.config(bg=self.bg_color, padx=50, pady=50)
        self.window.title("Flash Cards")
        self.flip_timer = self.window.after(3000, self.flip_card)

    def _create_canvas(self):
        """Creates the canvas and loads the front_image on it."""
        self.canvas = Canvas(width=800, height=526)
        self.front_image = PhotoImage(file="./images/card_front.png")
        self.back_image = PhotoImage(file="./images/card_back.png")
        self.canvas_image = self.canvas.create_image(400, 263, image=self.front_image)
        self.canvas.grid(row=0, column=0, rowspan=2)
        self.canvas.config(bg=self.bg_color, highlightthickness=0)

        self.language_text = self.canvas.create_text(400, 150, text="French", font=("Arial", 40))
        self.word_text = self.canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

    def _create_buttons(self):
        """Creates the app buttons."""
        self.wrong_image = PhotoImage(file="./images/wrong.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.config(command=self.new_card)
        self.wrong_button.grid(row=1, column=2)

        self.right_image = PhotoImage(file="./images/right.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.config(command=self.is_known)
        self.right_button.grid(row=0, column=2)


# Create a class object to start the app.
flash = FlashCard()
