# Import required modules.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

CITY_IATA_CODE = "your own city's IATA code"

# Get dates for today, tomorrow and day after 6 months.
today = datetime.now()
tomorrow = today + timedelta(days=1)
date_after_6_months = today + timedelta(days=180)

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Getting destinations data from the google sheet.
destinations = data_manager.get_destinations_data()

for destination in destinations:
    # If destination's IATA code not provided, get and add it to google sheet.
    if destination["iataCode"] == "":
        destination_iatacode = flight_search.get_iata_code(destination["city"])
        destination_id = destination["id"]
        data_manager.update_destination_iata_code(destination_id, destination_iatacode)

    # Look for available flights for the destination.
    flight_data = flight_search.get_available_flights(
            CITY_IATA_CODE, destination["iataCode"], tomorrow.strftime("%d/%m/%Y"),
            date_after_6_months.strftime("%d/%m/%Y")
    )

    # If flight_data returned and flight's price is less than the minimum price,
    # Send a price alert mail to the user.
    if flight_data and flight_data.price < destination["lowestPrice"]:
        # Send the emails with the flight details.
        if flight_data.stop_overs == 0:
            message = f'''Subject: Low Flight Price Alert!\n\n
                            Only ${flight_data.price} to fly 
                                From: {flight_data.origin_city}-{flight_data.origin_airport} 
                                To: {flight_data.destination_city}-{flight_data.destination_airport}
                            Between: {flight_data.out_date} and {flight_data.return_date}
                            
                            BOOK YOUR TICKETS NOW!
                        '''
            notification_manager.send_emails(message)
        else:
            message = f'''Subject: Low Flight Price Alert!\n\n
                            Only ${flight_data.price} to fly 
                                From: {flight_data.origin_city}-{flight_data.origin_airport} 
                                To: {flight_data.destination_city}-{flight_data.destination_airport}
                                    Flight has 1 stop over, via {flight_data.via_city}
                                Between: {flight_data.out_date} and {flight_data.return_date}

                                BOOK YOUR TICKETS NOW!
                        '''
            notification_manager.send_emails(message)
