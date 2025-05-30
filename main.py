from selenium import webdriver
# imported WebElement to assist with type-hinting
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import asyncio



# set up options, service, and initialize webdriver
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
# change the user-agent to get around robots.txt potentially blocking selenium
options.add_argument(f"user-agent={user_agent}")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Web-Scraping routine
driver.get("https://www.newsbreak.com/locations/michigan-state/cities")

# type-hint the elements list to aid in object-property queries
elements : list[WebElement] = driver.find_elements(By.XPATH, "//li/div/a")

e : WebElement = None
for e in elements:
    print(e.get_attribute("href"))

input("Press [Enter] to exit...")
driver.quit()