from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#for dynamically loaded website support

#for output file types support
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
        if options:
            self.options=options
        else:
            self.options=Options()
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument(f"user-agent={self.userAgent}")
            
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
        Quits the webdriver. This method should be called when
        finished scraping.
    '''
    def _quitDriver(self):
        self.driver.quit()
     
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
        