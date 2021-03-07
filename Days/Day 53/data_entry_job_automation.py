# Day 53 project - Data Entry Job Automation.

# Import required modules.
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time


chrome_web_driver = "your chrome driver location"
# User's Google form and Zillow(with desired filters) links.
google_form_link = "your own google form link."
zillow_endpoint = "your own url from zillow after applying filters."

# User's browser details.
# Copy and paste yours from "http://myhttpheader.com/".
headers = {
    "User-Agent": "",
    "Accept-Language": "",
}

# Getting zillow website data.
site_data = requests.get(url=zillow_endpoint, headers=headers)
site_data.raise_for_status()

# Scraping the received data.
soup = BeautifulSoup(site_data.text, "html.parser")
# Creating a list of links of all rentals.
all_rental_link_elements = soup.select(".list-card-top a")
all_rental_links = []
for rental in all_rental_link_elements:
    rental_link = rental["href"]
    # Handling incomplete links.
    if "http" not in rental_link:
        all_rental_links.append(f"https://www.zillow.com{rental_link}")
    else:
        all_rental_links.append(rental_link)

# Creating a list of address of all rentals.
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# Creating a list of prices of all rentals.
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    try:
        # Getting the price of a single listing.
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        # Getting the price of multiple listings.
        price = element.select(".list-card-details li")[0].contents[0]
        all_prices.append(price)
    else:
        all_prices.append(price)


# Creating responses for the google form.
# It is used to create the spreadsheet.
driver = webdriver.Chrome(executable_path=chrome_web_driver)
for no in range(len(all_rental_links)):
    # Opening the google form in chrome.
    driver.get(google_form_link)
    time.sleep(3)
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address_input.send_keys(all_addresses[no])
    price_input.send_keys(all_prices[no])
    link_input.send_keys(all_rental_links[no])
    submit_button.click()

driver.quit()
