from BaseScraper import BaseScraper


def main():
    loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    loadbypagination="https://webscraper.io/test-sites/e-commerce/static/phones/touch"
    loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    
    print('Scraping Dynamic Content - Load Button')
    baseScraper = BaseScraper(url=loadbybutton)
    baseScraper.scrapeXPATH_DynamicLoadButton(\
        xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]", xPathOfLoadMoreElement="//div/a[text()='More']", xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")
    print('Scraping Dynamic Content - Scroll to Load')
    baseScraper.setURL(loadbyscrolling)
    baseScraper.scrapeXPATH_DynamicScroll(\
        xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]", xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")
    print('Scraping Dynamic Content - Pagination')
    baseScraper.setURL(loadbypagination)
    baseScraper.scrapeXPATH_DynamicPagination(\
        xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]", xPathOfPaginationElement="//div[@id='static-pagination']/nav/ul[@class='pagination']/li/a[@rel='next']",xPathOfElementToScrape="//h4[@class='price float-end card-title pull-right']")
    baseScraper._quitDriver()
    pass


if __name__ == "__main__":
    main()