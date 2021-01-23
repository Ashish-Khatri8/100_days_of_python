# Day 33 project - ISS Overhead Notifier.

# Import required modules.
import requests
import datetime
import smtplib
from time import sleep

# User details.
my_email = "your_mail@gmail.com"
my_password = "your_mail_password"
my_latitude = 28.613939
my_longitude = 77.209023


def is_iss_overhead():
    """Returns True if ISS is close to user's location."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Check latitude and longitude difference with a margin of 5.
    if my_latitude-5 <= iss_latitude <= my_latitude+5:
        if my_longitude-5 <= iss_longitude <= my_longitude+5:
            return True


def is_night():
    """Returns True if it is night at user's location."""
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Get sunrise and sunset hours at user's location.
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # Get user's current time.
    current_time = datetime.datetime.now()
    current_hour = int(current_time.hour)

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True


# If ISS is nearby and its night, mail the user to look up in the sky.
while True:
    sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, to_addrs=my_email,
                msg="Subject: Look Up!\n\nThe ISS is above you in the sky!".encode("utf8")
            )
