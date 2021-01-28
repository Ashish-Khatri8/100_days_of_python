# Day 35 project - Rain Alert.

import requests
import smtplib

# User details.
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"

parameters = {
    "lat": "your city latitude's float value",
    "lon": "your city longitude's float value",
    "exclude": "current,minutely,daily",
    "appid": "your open_weather_map_API_Key",
}


def send_email():
    """Sends rain alert to the user given email."""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, to_addrs=EMAIL,
            msg="Subject: Bring your umbrella!\n\nIt's going to rain in the next 12 hours."
        )


def will_rain():
    """Returns True if it will rain in the next 12 hours at user's location."""
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    weather_data = response.json()["hourly"][:12]
    for next_hour in weather_data:
        weather_id = next_hour["weather"][0]["id"]
        # Weather ID of less than 700 means that it will rain.
        if int(weather_id) < 700:
            return True


# If it's going to rain, send the rain alert email.
if will_rain():
    send_email()
