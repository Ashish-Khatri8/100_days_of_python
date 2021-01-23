# Day 32 project - Automatic Birthday Wisher.

# Import required modules.
import datetime as dt
import smtplib
import random
import pandas

# Get today's day and month.
today = dt.datetime.now()
day = today.day
month = today.month

# Read data from "birthdays.csv"
data = pandas.read_csv("birthdays.csv")

# Enter your and recipient's mail.
senders_mail = "your_mail@gmail.com"
senders_password = "your_password"
recipient_mail = "recipient's_mail@gmail.com"

# Loop through the data and if today is someone's birthday,
# Send them a Happy Birthday mail.
for (index, row) in data.iterrows():
    if row.month == month and row.day == day:
        letter_file = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_file) as file:
            letter = file.read()
            letter_to_send = letter.replace('[NAME]', row["name"].title())
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Securing connection.
            connection.starttls()
            connection.login(user=senders_mail, password=senders_password)
            connection.sendmail(
                from_addr=senders_mail, to_addrs=recipient_mail,
                msg=f"Subject:Happy Birthday {row['name'].title()}!\n\n{letter_to_send}".encode("utf8")
            )
