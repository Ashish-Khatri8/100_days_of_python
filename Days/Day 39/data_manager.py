import requests

SHEETY_API_ENDPOINT = "your own google sheet api endpoint from Sheety."
SHEETY_AUTHENTICATION = "your own bearer authentication code form Sheety."


class DataManager:
    """A class to manage the google sheet using Sheety's API."""

    def __init__(self):
        """Initialize authentication header."""
        self.headers = {
            "Authorization": SHEETY_AUTHENTICATION
        }

    def get_destinations_data(self):
        """Returns data for all destinations from the google sheet."""
        response = requests.get(
            url=SHEETY_API_ENDPOINT,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()["prices"]

    def update_destination_iata_code(self, destination_id, iata_code):
        """
        Updates the destination's IATA code in the google sheet.
        :parameter destination_id: Destination's row number in google sheet.
        :parameter iata_code: New IATA code for the destination.
        """
        new_code = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(
            url=f"{SHEETY_API_ENDPOINT}/{destination_id}",
            headers=self.headers,
            json=new_code
        )
        response.raise_for_status()
