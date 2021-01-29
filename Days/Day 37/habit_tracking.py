# Day 37 project - Habit Tracking.

import requests
from datetime import datetime

# User details.
USERNAME = "your username"
USER_TOKEN = "your self generated token for pixela api"
headers = {
    "X-USER-TOKEN": USER_TOKEN,
}

# Getting today's date in yyyymmdd format.
today = datetime.now().strftime("%Y%m%d")

# Project API endpoints.
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph id.
graphID = "graph1"


# Creating new user account.
user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
new_user = requests.post(url=pixela_endpoint, json=user_params)
new_user.raise_for_status()


# Creating new graph.
graph_params = {
    "id": graphID,
    "name": "Running",
    "unit": "Kms",
    "type": "float",
    "color": "ajisai",
}
new_graph = requests.post(
    url=graph_endpoint, json=graph_params, headers=headers
)
new_graph.raise_for_status()


# Adding new pixel in graph.
new_pixel_endpoint = f"{graph_endpoint}/{graphID}"
new_pixel_params = {
    "quantity": "any float value",
    "date": today,
}
new_pixel = requests.post(
    url=new_pixel_endpoint, json=new_pixel_params, headers=headers
)
new_pixel.raise_for_status()


# Updating an existing pixel in graph.
update_endpoint = f"{graph_endpoint}/{graphID}/{today}"
update_data = {
    "quantity": "updated value",
}
updated_pixel = requests.put(
    url=update_endpoint, json=update_data, headers=headers
)
updated_pixel.raise_for_status()


# Deleting an existing pixel in graph.
deleting_endpoint = f"{graph_endpoint}/{graphID}/{today}"
deleted_pixel = requests.delete(url=deleting_endpoint, headers=headers)
deleted_pixel.raise_for_status()
