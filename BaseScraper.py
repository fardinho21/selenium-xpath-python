from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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
        
    def setOutputFilePath(self,path:str):
        self.outputFilePath=path
        
    def setURL(self, url:str):
        self.url=url
        
    def _scrape(self, xPath:str) -> list[WebElement]:
        if not self.driver is None:
            self.driver.get(self.url)
            return self.driver.find_elements(By.XPATH, xPath)
    def _quitDriver(self):
        self.driver.quit()
        
    

class StateAndCityScraper(BaseScraper):
    def __init__(self, service:Service=None, options:Options=None, url:str=""):
        super().__init__(service, options, url)

    def scrapeXPATH(self, xPath:str, attribute:str="", tagName:bool=False, text:bool=False, outputToFile:bool=False):
        elements:list[WebElement] = super()._scrape(xPath=xPath)
        e : WebElement=None
        output:list[str]=[]
        try:
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
            if outputToFile:    
                with open(self.outputFilePath, "x" ) as OUT:
                    for o in output:
                        OUT.write(o+"\n")
                    OUT.close()
                
        except Exception as E:
                print(E)
                
        
    def doneScraping(self):
        super()._quitDriver()