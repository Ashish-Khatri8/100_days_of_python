# Day 49 project - Automated LinkedIn Job Applications.

# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# User details.
LINKEDIN_EMAIL = "your linkedin account email"
LINKEDIN_PASSWORD = "your linkedin account password"
MOBILE_NO = "your mobile no"
chrome_driver_path = "your chrome driver full path"
JOBS_URl = "URL of linkedin page with jobs you want to apply for"

# Opening LinkedIn.
driver = webdriver.Chrome(chrome_driver_path)
driver.get(url=JOBS_URl)

# Signing in to LinkedIn.
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
# Entering email and password.
email = driver.find_element_by_id("username")
email.send_keys(LINKEDIN_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(LINKEDIN_PASSWORD)
password.send_keys(Keys.ENTER)


# Getting all jobs listed on the page.
all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

# Applying to all jobs found.
for job in all_jobs:
    print("Applying")
    job.click()
    sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        driver.execute_script("arguments[0].click();", apply_button)
        sleep(3)

        # Entering user's mobile number.
        mobile_no = driver.find_element_by_class_name("fb-single-line-text__input")
        if mobile_no.text == "":
            mobile_no.send_keys(MOBILE_NO)
        submit_button = driver.find_element_by_css_selector("footer button")

        # Skip if the submit_button is a "Next" button, as it will be a multi-step application.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Application skipped!")
            continue
        else:
            submit_button.click()
            print("Successfully applied!")

        # Once application completed, close the pop-up window.
        sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # Skip if already applied to job or job is no longer accepting applications.
    except NoSuchElementException:
        print("Not taking applications. Skipped!")
        continue

sleep(5)
driver.quit()
