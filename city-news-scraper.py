from BaseScraper import BaseScraper, CityScraper
import asyncio



cityScraper:CityScraper=CityScraper(url="https://quotes.toscrape.com/")

cityScraper.scrapeXPATH(xPath="//h1", text=True)