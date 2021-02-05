# Day 40 project - Flight Club.

import requests

USERS_SHEET_API_ENDPOINT = "your own 'Users' sheet endpoint from Sheety"
SHEETY_AUTHENTICATION = "your own bearer authentication code from sheety"
HEADER = {
    "Authentication": SHEETY_AUTHENTICATION
}


def join_club():
    print("\nWelcome to BLaze-K8's Flight Club.")
    print("We find the best flight deals and email you.\n")
    # Prompt user for first, last names and email.
    first_name = input("What is your first name?\t")
    last_name = input("What is your last name?\t")
    email = input("\nWhat is your email?\t")
    # Verify the email.
    email_verified = (input("Type your email again.\t") == email)
    if email_verified:
        add_new_user(first_name, last_name, email)


def add_new_user(f_name, l_name, mail):
    """Adds new user in the Users sheet."""
    new_user = {
        "user": {
            "firstName": f_name,
            "lastName": l_name,
            "email": mail,
        }
    }
    response = requests.post(url=USERS_SHEET_API_ENDPOINT, headers=HEADER, json=new_user)
    response.raise_for_status()
    if response.status_code == 200:
        print("\nSuccess!\nYour email has been added.\nYou're in the club!")


def get_emails():
    """Returns a list of all users emails from the Users sheet."""
    response = requests.get(url=USERS_SHEET_API_ENDPOINT, headers=HEADER)
    users = response.json()["users"]
    emails = []
    for user in users:
        emails.append(user["email"])
    return emails


if __name__ == '__main__':
    join_club()
