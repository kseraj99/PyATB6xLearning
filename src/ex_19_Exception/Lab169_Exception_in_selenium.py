from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

try:
    drive = webdriver.Chrome()
    drive.get("https://google.com")
    drive.find_element("id", "Not exist")
except NoSuchElementException:
    print("Element not found")
