from BaseScraper import BaseScraper

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EXPECTED_CONDS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

import time

'''
    XPathScraper class. Provides features for scraping WebElements via XPaths 
'''
class XPathScraper(BaseScraper):
    
    def __init__(self, service:Service=None, options:Options=None, url:str=""):
        super().__init__(service, options, url)
        
    '''
        Scrapes web elements via xpath for static content
    '''
    def scrapeXPATH(self, xPath:str, attribute:str="", tagName:bool=False, text:bool=False, fileTypeOutput:str=""):
        
        self.driver.get(self.url)

        #scrape elements 
        elements:list[WebElement] = self.driver.find_elements(By.XPATH, xPath)
        e : WebElement=None
        output:list[str]=[]
        try:
            #gather data from elements
            for e in elements:
                if tagName:
                    print(e.tag_name)
                    output.append(e.tag_name)
                elif attribute:
                    print(e.get_attribute(attribute))
                    output.append(e.get_attribute(attribute))
                elif text:
                    print(e.text)
                    output.append(e.text)
                    
            #write to file
            if fileTypeOutput:
                self.outputToFile(output, fileTypeOutput)
                            
        except Exception as E:
                print(E)
     
    '''
        Scrapes web elements via xpaths for dynamic content loaded by a "load" button
    '''
    def scrapeXPATH_DynamicLoadButton(self, xPathOfPresenceElement:str="", xPathOfLoadMoreElement:str="", xPathOfElementToScrape:str=""):
            if not xPathOfPresenceElement:
                print("xPath of presence element not specified.")
                return
            if not xPathOfLoadMoreElement:
                print("xPath of 'Load More' element not specified.")
                return 
            if not xPathOfElementToScrape:
                print('xPath of element to scrape not specified')
                return
            
            products:list[WebElement]=[]
            self.driver.get(self.url)
            WebDriverWait(self.driver, 5).until(EXPECTED_CONDS.presence_of_element_located((By.XPATH, xPathOfPresenceElement)))

            while True:
                try:
                    load_button = WebDriverWait(self.driver, 5).until(EXPECTED_CONDS.element_to_be_clickable((By.XPATH, xPathOfLoadMoreElement)))
                    self.driver.execute_script("arguments[0].click();", load_button)
                    time.sleep(2)

                except Exception as E:
                    print(E)
                    break
                

            products=self.driver.find_elements(By.XPATH, xPathOfPresenceElement)
            for p in products:
                print(p.find_element(By.XPATH, xPathOfElementToScrape).text)
    
    '''
        Scrapes web elements via xpaths for dynamic content loaded via scrolling
    '''
    def scrapeXPATH_DynamicScroll(self, xPathOfPresenceElement:str="", xPathOfElementToScrape:str=""):
        if not xPathOfPresenceElement:
            print("xPath of presence element not specified.")
            return
        if not xPathOfElementToScrape:
            print("xPath of element to scrape not specified")
            return
        
        products:list[WebElement]=[]
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EXPECTED_CONDS.presence_of_element_located((By.XPATH, xPathOfPresenceElement)))
        final_height = self.driver.execute_script("return document.body.scrollHeight")
        
        while True:
            try:
                self.driver.execute_script("return window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                next_height = self.driver.execute_script("return document.body.scrollHeight")
                if next_height == final_height:
                    break
                final_height=next_height
            except Exception as E:
                print(E)
                break
        products=self.driver.find_elements(By.XPATH, xPathOfPresenceElement)
        for p in products:
            print(p.find_element(By.XPATH, xPathOfElementToScrape).text)
        
    '''
        Scrapes web elements via xpaths for dynamic paginated content
    '''
    def scrapeXPATH_DynamicPagination(self, xPathOfPresenceElement:str="", xPathOfPaginationElement:str="", xPathOfElementToScrape:str="", xPathOther:list[str]=[]):
        if not xPathOfPresenceElement:
            print("xPath of presence element not specified.")
            return
        if not xPathOfPaginationElement:
            print("xPath of pagination element not specified.")
            return
        if not xPathOfElementToScrape:
            print("xPath of element to scrape not specified.")
            return
        products:list[WebElement]=[]
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EXPECTED_CONDS.presence_of_all_elements_located((By.XPATH, xPathOfPresenceElement)))
        while True:
            try:
                catalog:WebElement=self.driver.find_element(By.XPATH, xPathOfPresenceElement)
                products=catalog.find_elements(By.XPATH, xPathOfElementToScrape)
                for p in products:
                    print(p.text)
                pagination_next = self.driver.find_element(By.XPATH, xPathOfPaginationElement)
                self.driver.execute_script("arguments[0].click();", pagination_next)
                time.sleep(1)
            except Exception as E:
                # print(E)
                print("Pagination End")
                break