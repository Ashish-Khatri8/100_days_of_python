# Day 50 project - Auto Tinder Swiping Bot.

# Import required modules.
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

# User details.
FACEBOOK_EMAIL = "your facebook email id"
FACEBOOK_PASSWORD = "your facebook password"
chrome_web_driver = "your chrome driver location"


# Logging in to Tinder.
driver = webdriver.Chrome(executable_path=chrome_web_driver)
driver.get(url="https://tinder.com/")
sleep(2)
log_in_button = driver.find_element_by_xpath(
    '//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in_button.click()
sleep(2)

# Logging in to Facebook popup window.
try:
    facebook_login = driver.find_element_by_xpath(
        '//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button')
except NoSuchElementException:
    more_options = driver.find_element_by_xpath(
        '//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    facebook_login = driver.find_element_by_xpath(
        '//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]/button')
finally:
    tinder_window = driver.current_window_handle
    facebook_login.click()
    sleep(3)
    # Switching to facebook login popup window.
    for handle in driver.window_handles:
        if handle != tinder_window:
            fb_login_window = handle
    driver.switch_to.window(fb_login_window)
    # Entering email and password.
    email_entry = driver.find_element_by_id("email")
    password_entry = driver.find_element_by_id("pass")
    sleep(3)
    email_entry.send_keys(FACEBOOK_EMAIL)
    password_entry.send_keys(FACEBOOK_PASSWORD)
    password_entry.send_keys(Keys.ENTER)
    
    # Switching back to tinder window.
    driver.switch_to.window(tinder_window)


# Allow location access, cookies and disallow notifications.
sleep(5)
location_allow = driver.find_element_by_xpath(
    '//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
sleep(3)
cookies_allow = driver.find_element_by_xpath(
    '//*[@id="t--1032254752"]/div/div[2]/div/div/div[1]/button')
cookies_allow.click()
sleep(3)
no_notifications = driver.find_element_by_xpath(
    '//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]')
no_notifications.click()
sleep(3)


# Now swipe right/ like on 100 profiles.
# Tinder provides only 100 likes per day for free tier.
for _ in range(100):
    # Waits for 3 seconds before liking next profile.
    sleep(3)
    try:
        like = driver.find_element_by_xpath(
            '//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    except NoSuchElementException:
        sleep(5)
        like = driver.find_element_by_xpath(
            '//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    finally:
        try:
            like.click()
        except ElementClickInterceptedException:
            sleep(2)
            try:
                # Clicks on "Not Interested" if "Add tinder to home screen" window pops up.
                not_int = driver.find_element_by_xpath(
                    '//*[@id="t-1222506740"]/div/div/div[2]/button[2]')
                not_int.click()
                sleep(2)
                like.click()
            except NoSuchElementException:
                # Clicks on "Dismiss" if "Send super like" window pops up.
                dismiss = driver.find_element_by_xpath(
                    '//*[@id="t-1222506740"]/div/div/button[2]')
                dismiss.click()

# Close the browser window.
driver.quit()
