import requests
from flight_data import FlightData

TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "Your own API key from tequila."


class FlightSearch:
    """A class to search for flights using Tequila Flight Search API."""

    def __init__(self):
        """Initialize API header."""
        self.headers = {
            "apikey": TEQUILA_API_KEY,
        }

    def get_iata_code(self, city_name):
        """Returns IATA code for the city_name."""
        parameters = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(
            url=f"{TEQUILA_API_ENDPOINT}/locations/query",
            headers=self.headers,
            params=parameters,
        )
        response.raise_for_status()
        city_iata_code = (response.json()["locations"][0]["code"])
        return city_iata_code

    def get_available_flights(self, departure_code, destination_code, start_date, end_date):
        """Returns flight details for available flights with 0 or 1 stopover."""
        parameters = {
            "fly_from": departure_code,
            "fly_to": destination_code,
            "dateFrom": start_date,
            "dateTo": end_date,
            "adults": 1,
            "curr": "USD",
            "flight_type": "round",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }
        response = requests.get(
            url=f"{TEQUILA_API_ENDPOINT}/v2/search",
            params=parameters,
            headers=self.headers
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            # If there is no direct flight, look for a flight with 1 stop over.
            parameters["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_API_ENDPOINT}/v2/search",
                params=parameters,
                headers=self.headers
            )
            # If no flight return None, else return flight_details.
            if len(response.json()["data"]) < 1:
                return None
            else:
                data = response.json()["data"][0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
