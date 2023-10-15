# Import the selenium module
from selenium import webdriver

# Create a driver object that will control the browser
driver = webdriver.Chrome()

# Use the driver object to perform various actions, such as opening a web page
driver.get("https://www.bing.com")