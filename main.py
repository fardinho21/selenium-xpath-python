from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://quotes.toscrape.com/")

element = driver.find_element(By.XPATH, "//h1")

print(element.text)

input("Press [Enter] to exit...")
driver.quit()