from BaseScraper import BaseScraper


def main():
    loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    loadbypagination="https://webscraper.io/test-sites/e-commerce/static/phones/touch"
    loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    
    print('Scraping Dynamic Content - Load Button')
    baseScraper = BaseScraper(url=loadbybutton)
    baseScraper.scrapeXPATH_DynamicLoadButton()
    print('Scraping Dynamic Content - Scroll to Load')
    baseScraper.setURL(loadbyscrolling)
    baseScraper.scrapeXPATH_DynamicScroll()
    print('Scraping Dynamic Content - Pagination')
    baseScraper.setURL(loadbypagination)
    baseScraper.scrapeXPATH_DynamicPagination()
    baseScraper._quitDriver()
    pass


if __name__ == "__main__":
    main()