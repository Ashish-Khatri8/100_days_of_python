# Day 28 project - Pomodoro app.

# Import tkinter module.
from tkinter import *


class Pomodoro:
    """A class to represent the Pomodoro app."""
    def __init__(self):
        """Initialize app attributes and methods."""
        self.timer = None
        self.round_no = 0
        # Time in minutes for work, break and rest. 
        self.break_time = 5
        self.work_time = 25
        self.rest_time = 15
        self.bg_color = "old lace"
        self._create_window()
        self._create_labels()
        self._create_buttons()
        self._create_canvas()
        self.window.mainloop()

    def _create_window(self):
        """A method that creates the app window."""
        self.window = Tk()
        self.window.title("Pomodoro App")
        self.window.minsize(width=300, height=300)
        self.window.config(padx=100, pady=50, bg=self.bg_color)

    def _create_labels(self):
        """A method that creates the app labels. """
        # Timer label, prints Timer/ Work/ Break/ Rest on window..
        self.timer_label = Label(text="Timer", font=("Arial", 40, "bold"))
        self.timer_label.grid(row=0, column=1)
        self.timer_label.config(fg="dark slate blue", bg=self.bg_color)

        # Check sign(✔) label.
        self.check_label = Label(text="", font=("Arial", 30))
        self.check_label.grid(row=3, column=1)
        self.check_label.config(fg="green", bg=self.bg_color)

    def _create_buttons(self):
        """A method that creates the app buttons."""
        # Start button.
        self.start_button = Button(text="Start", highlightthickness=0, font=("Arial", 15))
        self.start_button.grid(row=2, column=0)
        self.start_button.config(command=self.start_timer, fg="white", bg="dark slate blue")

        # Reset button.
        self.reset_button = Button(text="Reset", highlightthickness=0, font=("Arial", 15))
        self.reset_button.grid(row=2, column=2)
        self.reset_button.config(command=self.reset_timer, fg="white", bg="dark slate blue")

    def _create_canvas(self):
        """A method that creates the canvas with tomato image and text."""
        self.canvas = Canvas(width=200, height=230, bg=self.bg_color, highlightthickness=0)
        self.tomato_image = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_image)
        self.timer_text = self.canvas.create_text(
            100, 130, text="00:00", font=("Arial", 30, "bold"), fill="white")
        self.canvas.grid(row=1, column=1)

    def start_timer(self):
        """A method that starts the timer."""
        # Disable the start button when the timer is active.
        self.start_button["state"] = "disabled"

        # If round_no is divisible by 2, its working round, every 8th round is rest round.
        # All other rounds are 5 minute break rounds. Rounds are 0-7.
        if self.round_no % 2 == 0:
            round_time = self.work_time
            self.timer_label.config(text="Work", fg="green")
            # Completely hide the window.
            self.window.iconify()
            self.window.withdraw()

        elif self.round_no % 7 == 0:
            # Show the window on screen.
            self.window.deiconify()
            round_time = self.rest_time
            self.timer_label.config(text="Rest", fg="black")

        else:
            # Show the window on screen.
            self.window.deiconify()
            round_time = self.break_time
            self.timer_label.config(text="Break", fg="red")

        # Draw a ✔ on window after completion of a work round.
        if self.round_no > 0:
            self.check_label.config(text="✔" * ((self.round_no+1)//2))
        # Pass the time in seconds to count_down method.
        self.count_down(round_time * 60)

    def reset_timer(self):
        """A function to reset the app."""
        # Activate the Start button.
        # And reset everything when user clicks on reset button.
        self.start_button["state"] = "normal"
        self.window.after_cancel(self.timer)
        self.timer_label.config(text="Timer", fg="dark slate blue")
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_label.config(text="")

    def count_down(self, count):
        """A function to keep the timer working."""
        seconds = count % 60
        minutes = count // 60
        if seconds < 10:
            seconds = f"0{seconds}"
        if minutes < 10:
            minutes = f"0{minutes}"
        self.canvas.itemconfig(self.timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.round_no += 1
            self.start_timer()


# Create a class object to start the app.
pomodoro = Pomodoro()
