# Day 52 project - Instagram follower bot.

# Sends a follow request to all the followers of the target account.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import math


# User details.
USERNAME = "your instagram username/email id"
PASSWORD = "your instagram password"
TARGET_ACCOUNT = "Account whose followers to follow"
chrome_web_driver = "your chrome driver location"


class InstaFollower:
    """A class to represent the Instagram Follower Bot."""
    def __init__(self):
        """Initializes the selenium web driver."""
        self.driver = webdriver.Chrome(executable_path=chrome_web_driver)

    def login(self):
        """Logs In the user in instagram."""
        self.driver.get(url="https://www.instagram.com/accounts/login/")
        sleep(3)

        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        sleep(3)
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        """Finds all the followers of the target account."""
        self.driver.get(url=f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        
        followers_count = int(self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
            ).get_attribute("title").replace(',', ''))
        
        followers.click()
        sleep(2)

        scrolls_required = math.ceil((followers_count - 12) // 12) + 1
        followers_list = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        
        for i in range(scrolls_required):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            sleep(2)

    def follow(self):
        all_follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_elements_by_css_selector(".mt3GC button")[1]
                cancel_button.click()


if __name__ == '__main__':
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
