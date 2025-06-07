from BaseScraper import BaseScraper
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EXPECTED_CONDS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#beautiful soup
from bs4 import BeautifulSoup
from bs4._typing import _QueryResults
#other imports
import time


class BeautifulSoupScraper(BaseScraper):
    soup:BeautifulSoup=None
    def __init__(self, service:Service=None, options:Options=None, url:str=""):
        super().__init__(service, options, url)
        
        
    def scrapeBeautifulSoupStatic(self, htmlElementTag:str="", htmlClassAttributes:str=""):
        self.driver.get(self.url)
        time.sleep(3)
        

        html=self.driver.page_source
        self.soup=BeautifulSoup(html, 'html.parser')
        
        if htmlClassAttributes:
            elements: _QueryResults = self.soup.find_all(htmlElementTag, class_=htmlClassAttributes.split(" "))
            for result in elements:
                print(result.get_text())


    def scrapeBeautifulSoup_DynamicLoadButton(self, presenceElementCSS:str="", elementsToScrape:dict[str,str]=dict()):
        
        self.driver.get(self.url)
        while True:
            try:
                load_button = WebDriverWait(self.driver, 5).until(EXPECTED_CONDS.element_to_be_clickable((By.CSS_SELECTOR, presenceElementCSS)))
                self.driver.execute_script("arguments[0].click();", load_button)
                time.sleep(2)
                pass
            except Exception as E:
                print(E)
                break
            
        html=self.driver.page_source
        self.soup=BeautifulSoup(html, 'html.parser')
        prices:str=[]
        names:str=[]
        for tag,attributes in elementsToScrape.items():
            elements: _QueryResults = self.soup.find_all(tag, class_=attributes.split(" "))
            for result in elements:
                if tag=="h4":
                    prices.append(result.get_text())
                elif tag=="a":
                    names.append(result.get_text())
        
        pairs=zip(names,prices)
        for e in pairs:
            print(e)
                
            
        
        pass