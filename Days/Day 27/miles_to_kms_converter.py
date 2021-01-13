# Day 27 project - Miles to KiloMeters Converter.

# Import tkinter module.
import tkinter

# Create the window.
window = tkinter.Tk()
window.title("Miles to KiloMeters Converter")
window.minsize(height=300, width=300)
window.config(padx=50, pady=50, bg="light steel blue")

# Create all the labels.
font = ("Arial", 20, "bold")
bg_color = "light steel blue"
miles_label = tkinter.Label(text="miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=20, pady=20, bg=bg_color, font=font)

kms_label = tkinter.Label(text="kilometers")
kms_label.grid(row=1, column=2)
kms_label.config(padx=20, pady=20, bg=bg_color, font=font)

are_equal_to_label = tkinter.Label(text="are equal to")
are_equal_to_label.grid(row=1, column=0)
are_equal_to_label.config(padx=20, pady=20, bg=bg_color, font=font)

output_label = tkinter.Label(text="0")
output_label.grid(row=1, column=1)
output_label.config(padx=20, pady=20, bg=bg_color, font=font, foreground="green")

# Get user input.
user_input = tkinter.Entry()
user_input.grid(row=0, column=1)
user_input.focus()
user_input["width"] = 20


# Function to convert miles to kilometers.
def convert_miles_to_kms():
    no_of_miles = float(user_input.get())
    no_of_kms = round(no_of_miles * 1.60934, 2)
    output_label["text"] = no_of_kms


# Create the button.
button = tkinter.Button(text="Calculate")
button.config(command=convert_miles_to_kms)
button.grid(row=2, column=1)
button.config(padx=20, pady=20, bg='black', foreground='white', font=font)

# Window should close when the user exits.
window.mainloop()
