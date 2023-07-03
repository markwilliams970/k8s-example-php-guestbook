import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Instantiate chromedriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Guestbook url
guestbook_url="http://guestbook.synthesis-analytics.com"
browser.get(guestbook_url)

# Locate input field
message = browser.find_element(By.NAME, "input")

# Input some random text
my_uuid = str(uuid.uuid4())
message.send_keys(my_uuid)

# Submit the form
submit_button = browser.find_element(By.XPATH, '//button[normalize-space()="Submit"]')
submit_button.click()
