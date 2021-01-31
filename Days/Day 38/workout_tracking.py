# Day 38 project - Workout Tracking using Google Sheets.

import requests
from datetime import datetime

# User details.
GENDER = "your gender"
WEIGHT_KG = 00.00  # Your weight in kilograms
HEIGHT_CM = 000.0  # Your height in centimetres
AGE = 00           # Your age

# User secret keys.
NUTRITIONIX_APP_KEY = "your own nutritionix app key"
NUTRITIONIX_APP_ID = "your own nutritionix app id"
SHEETY_AUTHENTICATION = "your own bearer authorization token from Sheety"

# API Endpoints.
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "your own sheet's POST request url from Sheety"

# Get today's date and current time.
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


# Headers for both POST requests.
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

sheety_headers = {
    "Authorization": SHEETY_AUTHENTICATION
}

# Prompt user for entering exercises done today.
exercises = input("Tell me which exercises you did: ")
exercise_data = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# POST request to NUTRITIONIX API.
response = requests.post(
    url=nutritionix_exercise_endpoint, json=exercise_data, headers=nutritionix_headers
)
response.raise_for_status()
data = response.json()["exercises"]

# Saving data to google sheets using Sheety API.
for each_exercise in data:
    duration = each_exercise["duration_min"]
    calories = each_exercise["nf_calories"]
    exercise = each_exercise["name"]

    workout_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_response = requests.post(
        url=sheet_endpoint, json=workout_data, headers=sheety_headers
    )
    sheety_response.raise_for_status()
