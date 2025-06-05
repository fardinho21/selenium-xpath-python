from BaseScraper import BaseScraper


def main():
    loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    loadbypagination="https://webscraper.io/test-sites/e-commerce/static/phones/touch?page=1"
    loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    baseScraper = BaseScraper(url=loadbybutton)
    baseScraper.scrapeXPATH_DynamicLoadButton()
    baseScraper.setURL(loadbyscrolling)
    baseScraper.scrapeXPATH_DynamicScroll()
    # baseScraper.setURL(loadbypagination)
    # baseScraper.scrapeXPATH_DynamicPagination()
    baseScraper._quitDriver()
    pass


if __name__ == "__main__":
    main()