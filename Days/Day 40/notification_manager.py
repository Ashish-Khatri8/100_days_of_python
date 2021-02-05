import smtplib
from flight_club import get_emails

EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password@blaze"

# Get the list of emails from the "users" sheet.
emails = get_emails()


class NotificationManager:
    """"A class to send email notifications with flight details to all the users."""

    def send_emails(self, message):
        for email in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL, to_addrs=email, msg=message.encode("utf-8")
                )
