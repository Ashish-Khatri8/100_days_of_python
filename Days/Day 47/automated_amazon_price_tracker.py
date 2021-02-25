# Day 47 project - Automated Amazon Price Tracker.

from bs4 import BeautifulSoup
import requests
import smtplib


# User details.
EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"


# Product details.
MINIMUM_BUY_PRICE = 0.0   # Minimum price you want to buy the product for.
PRODUCT_URL = "copy and paste the url of amazon product you want here"


# User's browser details.
# Go to "http://myhttpheader.com/" and copy and paste the following details here.
USER_AGENT = "your browser's User-Agent"
ACCEPT_LANGUAGE = "your browser's Accept-Language"


# Scraping the product webpage.
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}
response = requests.get(url=PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


# Getting the product's name and current price.
product_name = soup.find(id="productTitle").getText().strip().capitalize()
product_price = soup.find(id="priceblock_ourprice").getText().split()[1].replace(",", "_")


# Checking if current product price is less than minimum buy price.
if float(product_price) < MINIMUM_BUY_PRICE:
    # If its less, send an email alert with the product link.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        message_body = f"{product_name} is now available for only {product_price}!\n{PRODUCT_URL}"
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message_body}".encode("utf-8")
        )
