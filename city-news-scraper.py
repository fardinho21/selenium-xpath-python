from BaseScraper import BaseScraper, StateAndCityScraper
import asyncio
import re
import time

#Iterate through Newsbreak-All-States.txt
# Set the output file path to the STATENAME.txt
# Set the URL to the newsbreak url for the state
# for each city in the state, gather the newsbreak link for the associated local news source

gFileNames:dict=dict() # key : STATE.txt; value: newsmax link to locations/<state>/cities
with open('./news-sources/Newsbreak-All-States.txt', 'r') as NEWSBREAK:

    for link in NEWSBREAK:
        match:re.Match[str]=re.search(r'(locations\/)([a-z\-]*)(\/cities)', link)
        
        gFileNames[(match.group().split("/")[1].upper())] = link
    
    NEWSBREAK.close()
    

stateAndCityScraper:StateAndCityScraper=StateAndCityScraper()
for stateFileName, newsBreakLink in gFileNames.items():
    stateAndCityScraper.setURL(newsBreakLink[:-1])
    stateAndCityScraper.setOutputFilePath("./news-sources/"+stateFileName)
    stateAndCityScraper.scrapeXPATH("//li/div/a", attribute="href", fileTypeOutput="json")
    time.sleep(120)

stateAndCityScraper.doneScraping()