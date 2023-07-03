import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

# Instantiate chromedriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Guestbook url
guestbook_url="http://guestbook.synthesis-analytics.com"
browser.get(guestbook_url)

# Locate input field
message = browser.find_element(By.NAME, "input")

# Locate submit button
submit_button = browser.find_element(By.XPATH, '//button[normalize-space()="Submit"]')

# Read input data and submit to the webform
with (open('submit-data.csv', newline='')) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row)
    submit_message = row['Date'] + ": " + row['UniqueID']
    message.send_keys(submit_message)
    submit_button.click()
