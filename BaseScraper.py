from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#for dynamically loaded website support
from selenium.webdriver.support import expected_conditions as EXPECTED_CONDS
from selenium.webdriver.support.ui import WebDriverWait

#for output file types support
import csv
import json
import xml.etree.ElementTree as XML_ETREE

#other imports
import time


'''
    BaseScraper base class. Provides basic set up and utility functions
    for scraping data and file-output features 
'''
class BaseScraper:
    options:Options=None
    service:Service=None
    url:str=""
    userAgent:str="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    driver: WebDriver=None
    outputFilePath:str=""
    
    def __init__(self, service:Service=None, options:Options=None, url:str=""):
        if service:
            self.service = service
        else:
            self.service=Service(ChromeDriverManager().install())
        if options is None:
            self.options=Options()
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument(f"user-agent={self.userAgent}")
        else:
            self.options=options
            
        self.url=url
        self.driver=webdriver.Chrome(service=self.service, options=self.options)
        
    '''
        Sets the output file path member variable.
    '''
    def setOutputFilePath(self,path:str):
        self.outputFilePath=path
        
    '''
        Sets the URL member variable
    '''
    def setURL(self, url:str):
        self.url=url

    '''
        Scrapes elements via XPath from the URL provided at construction.
        Returns a list of WebElements
    '''
    def _scrape(self, xPath:str) -> list[WebElement]:
        if not self.driver is None:
            self.driver.get(self.url)
            return self.driver.find_elements(By.XPATH, xPath)
        
    '''
        Quits the webdriver. This method should be called when
        finished scraping.
    '''
    def _quitDriver(self):
        self.driver.quit()
        
    '''
        Scrapes elements specified by an XPath
        and optionally gathers the element's attribute, tag name, or text.
        It also optionally outputs the contents of the data to either a txt, csv, xml, or json file.
        Compatible with static web pages.
    '''
    def scrapeXPATH(self, xPath:str, attribute:str="", tagName:bool=False, text:bool=False, fileTypeOutput:str=""):
        if self.scrapeDynamicSite is False:
            print("Website contains dynamically loaded content.")
            return
    
        #scrape elements 
        elements:list[WebElement] = self._scrape(xPath=xPath)
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
        Scrapes dynamically loaded content.
        loaderType specifies how the dynamic content is loaded (button, scroll, pagination)
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
            


    
    '''
        Writes scraped data to an output file of a specified format.
        Supported file types are txt, csv, xml, and json.
    '''   
    def outputToFile(self, data:list[str], fileType:str="txt"):
        if fileType=="txt":
                with open(self.outputFilePath+".txt", "x" ) as OUT:
                    for o in data:
                        OUT.write(o+"\n")
                    OUT.close()
        elif fileType=="csv":
            with open(self.outputFilePath+".csv", "x", newline='') as CSV:
                fieldnames=['link']
                writer = csv.DictWriter(CSV, fieldnames=fieldnames)
                writer.writeheader()
                for o in data:
                    writer.writerow({"link":o})
                CSV.close()
        elif fileType=="json":
            dataToSave:dict=dict()
            for n,o in enumerate(data):
                dataToSave[n]={"link":o}
            with open(self.outputFilePath+".json", "x") as JSON:
                JSON.write(json.dumps(dataToSave))
                JSON.close()
        elif fileType=="xml":
            root = XML_ETREE.Element("CityNewsSources")
            for o in data:
                
                newsSource = XML_ETREE.Element("news-source")
                newsSource.text = o
                root.append(newsSource)
                
            tree =XML_ETREE.ElementTree(root)
            tree.write(self.outputFilePath+".xml")
        else:
            print("File type not supported.")
        
    def printScrapedElements(self, elements:list[WebElement], xPathsOfTextContainingElementsToScrape:list[str]=[]):
        print(len(xPathsOfTextContainingElementsToScrape))
        if len(xPathsOfTextContainingElementsToScrape) == 0:
            print("No paths of text containing elements to scrape provided")
            return
        
        for e in elements:
            for xp in xPathsOfTextContainingElementsToScrape:
                print(e.find_element(By.XPATH, xp).text)