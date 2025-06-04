from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json
import xml.etree.ElementTree as XML_ETREE


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
    '''
    def scrapeXPATH(self, xPath:str, attribute:str="", tagName:bool=False, text:bool=False, fileTypeOutput:str=""):
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
        
        
