# Day 30 project - Improved Password Manager App(JSON + Error Handling).

# Import required modules.
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


class PasswordManager:
    """A class to represent the Password Manager app."""
    def __init__(self):
        """Initialize app attributes and methods."""
        self.bg_color = "light steel blue"
        self.font = ("Arial", 12, "bold")
        self._user_interface_setup()
        self.window.mainloop()

    def _user_interface_setup(self):
        """Creates the whole user interface."""
        self._create_window()
        self._create_canvas()
        self._create_labels()
        self._create_entries()
        self._create_buttons()

    def search_website(self):
        """
        Looks for website user searched for in saved data.
        If website data exists, shows the entire data associated with it.
        """
        site = self.website_entry.get()
        try:
            with open("passwords.json") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found.")
        else:
            if site in data:
                message = f"\nUsername :\n\t{data[site]['username']}\n\nEmail :\n\t{data[site]['email']}\n\n" \
                         f"Password :\n\t{data[site]['password']}\n"
                messagebox.showinfo(title=site, message=message)
            else:
                messagebox.showerror(title="Error", message=f"No details for the website \"{site}\" exists.")

    def save_details(self):
        """Saves the details to the json file when user clicks on Add button."""
        # Get user input from all entry widgets.
        website = self.website_entry.get()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check if user has not left any field blank.
        if self.check_entries(website, username, email, password):
            # Create a dictionary of the new_data to be stored.
            new_data = {
                f"{website}": {
                    "username": username,
                    "email": email,
                    "password": password,
                }
            }
            message = f"You entered :\n\nWebsite :\n\t{website}\n\nUsername :\n\t{username}\n\n" \
                      f"Email :\n\t{email}\n\nPassword :\n\t{password}\n\nSave the details?"

            # Prompt user to check all the entered details.
            should_save = messagebox.askokcancel(title="Check details.", message=message)
            # If user clicks "OK", save all the details to the json file.
            if should_save:
                self.save_to_file(new_data)

    def save_to_file(self, new_data):
        """Saves the new data to the passwords.json file."""
        try:
            with open("passwords.json") as file:
                # Read the old data.
                data = json.load(file)
                # Update the old data with new data.
                data.update(new_data)
        except FileNotFoundError:
            # Create the file and save data in it, if it does not exist.
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                # Save the updated data in the file.
                json.dump(data, file, indent=4)
        finally:
            # Clear all the user entries.
            self.clear_entries()
            # Tell the user that details are successfully saved.
            messagebox.showinfo(title="Saved", message="Details saved successfully.")

    def check_entries(self, website, username, email, password):
        """Returns True if none of the entries is empty, otherwise returns False."""
        if len(website) < 1 or len(username) < 1 or len(email) < 1 or len(password) < 1:
            messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
            return False
        return True

    def clear_entries(self):
        """Clears the user input from entries after data is saved to the json file."""
        self.website_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.website_entry.focus()

    def generate_password(self):
        """Generates a random password and inserts it in password entry."""
        # Delete any previously generated password from password entry.
        self.password_entry.delete(0, END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '<', '>', '_', '|', '^']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_list = password_letters + password_numbers + password_symbols
        # Shuffle the password_list to mix letters, numbers and symbols.
        shuffle(password_list)
        # Create a string from the list.
        password = "".join(password_list)
        # Insert the generated password in the password entry.
        self.password_entry.insert(0, password)

    def _create_window(self):
        """Creates the app window."""
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg=self.bg_color)

    def _create_canvas(self):
        """Creates a canvas with the logo on it."""
        self.canvas = Canvas(width=200, height=200)
        self.canvas.config(bg=self.bg_color, highlightthickness=0)
        self.lock_image = PhotoImage(file="logo.png")
        self.canvas.create_image(140, 100, image=self.lock_image)
        self.canvas.grid(row=0, column=1)

    def _create_labels(self):
        """Creates all the app label widgets."""
        # Website label.
        self.website_label = Label(text="Website:", font=self.font)
        self.website_label.config(pady=5, bg=self.bg_color)
        self.website_label.grid(row=1, column=0)

        # Username label.
        self.username_label = Label(text="Username:", font=self.font)
        self.username_label.config(pady=5, bg=self.bg_color)
        self.username_label.grid(row=2, column=0)

        # Email label.
        self.email_label = Label(text="Email:", font=self.font)
        self.email_label.config(pady=5, bg=self.bg_color)
        self.email_label.grid(row=3, column=0)

        # Password label.
        self.password_label = Label(text="Password:", font=self.font)
        self.password_label.config(pady=5, bg=self.bg_color)
        self.password_label.grid(row=4, column=0)

    def _create_entries(self):
        """Creates all the app entry widgets."""
        # Website entry.
        self.website_entry = Entry(width=20)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()

        # Username entry.
        self.username_entry = Entry(width=40)
        self.username_entry.grid(row=2, column=1, columnspan=2)

        # Email entry.
        self.email_entry = Entry(width=40)
        self.email_entry.grid(row=3, column=1, columnspan=2)

        # Password entry.
        self.password_entry = Entry(width=20)
        self.password_entry.grid(row=4, column=1)

    def _create_buttons(self):
        """Creates all the app button widgets."""
        # Search button.
        self.search_button = Button(text="Search", command=self.search_website)
        self.search_button.config(width=17, bg="green", fg="white", pady=5)
        self.search_button.grid(row=1, column=2)

        # Generate Password button.
        self.generate_password_button = Button(text="Generate Password", command=self.generate_password)
        self.generate_password_button.config(width=17, pady=5, fg="white", bg="green")
        self.generate_password_button.grid(row=4, column=2)

        # Add button.
        self.add_button = Button(text="Add", command=self.save_details)
        self.add_button.config(width=30, bg="black", fg="white")
        self.add_button.grid(row=5, column=1, columnspan=2)


# Create a class object to run the app.
password_manager = PasswordManager()
