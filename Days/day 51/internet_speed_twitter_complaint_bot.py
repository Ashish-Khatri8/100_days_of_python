# Day 51 project - Internet Speed Twitter Complaint Bot.

# Tweets a complaint to your internet service provider(ISP),
# If your current internet speed is less than the minimum speed promised.

# Import required modules.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# User details.
TWITTER_EMAIL = "your twitter email id"
TWITTER_PASSWORD = "your twitter account password"
chrome_web_driver = "your chrome driver location"

# ISP details.
MIN_UPLOAD_SPEED = 0    # Minimum upload speed promised by your ISP.
MIN_DOWNLOAD_SPEED = 0  # Minimum download speed promised by your ISP.
ISP_TWEETER_HANDLE = "@ your ISP's twitter handle."


class InternetSpeedTwitterBot:
    """A class to represent the Twitter Complaint Bot."""
    def __init__(self):
        """Initializes the selenium driver."""
        self.driver = webdriver.Chrome(executable_path=chrome_web_driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Gets your current upload and download speed."""
        self.driver.get(url="https://www.speedtest.net/")
        self.driver.implicitly_wait(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        # Waiting until speed check is completed, checking every 10 seconds.
        speed_check = ec.presence_of_element_located((
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div'
                      '/div[2]/div[3]/div/div/div[2]/div/div/ul[2]/li[2]'))
        WebDriverWait(self.driver, 1000, poll_frequency=10).until(speed_check)

        # Getting download and upload speed.
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
            'div[1]/div[2]/div/div[2]/span').text

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
            'div[1]/div[3]/div/div[2]/span').text

        # Printing internet speed.
        print(f"\nYour internet speed :-\n\tUpload speed: {self.up}Mbps\n\tDownload speed: {self.down}Mbps\n")

    def tweet_at_provider(self):
        """Tweets a complaint to the ISP whenever internet speed goes below minimum promised speed."""
        self.driver.get(url="https://twitter.com/login")
        self.driver.implicitly_wait(3)
        # Logging in to Twitter.
        email_entry = self.driver.find_element_by_name("session[username_or_email]")
        password_entry = self.driver.find_element_by_name("session[password]")
        self.driver.implicitly_wait(3)
        email_entry.send_keys(TWITTER_EMAIL)
        password_entry.send_keys(TWITTER_PASSWORD)
        password_entry.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)

        # Tweeting the complaint.
        tweet_box = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/'
            'div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey {ISP_TWEETER_HANDLE}, why is my internet speed {self.down}down/{self.up}up Mbps," \
                f"when I pay for a minimum {MIN_DOWNLOAD_SPEED}down/{MIN_UPLOAD_SPEED}up Mbps?"
        tweet_box.send_keys(tweet)
        self.driver.implicitly_wait(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div'
            '/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        self.driver.implicitly_wait(3)
        self.driver.quit()


# If current internet speed is less than the promised speed, tweet a complaint.
if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    if float(bot.up) < MIN_UPLOAD_SPEED and float(bot.down) < MIN_DOWNLOAD_SPEED:
        bot.tweet_at_provider()
        print("Tweeted a complaint to your ISP as you are getting low speed!")
    else:
        bot.driver.quit()
        print("You are getting the promised speed, so no need to complaint.")
