import smtplib

EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"


class NotificationManager:
    """"A class to send email notifications with the flight details."""
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL, to_addrs=EMAIL, msg=message.encode("utf-8")
            )
