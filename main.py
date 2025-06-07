from BaseScraper import BaseScraper
from XPathScraper import XPathScraper
from BeautifulSoupScraper import BeautifulSoupScraper
def main():
    
    # loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    # loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    loadbypagination="https://webscraper.io/test-sites/e-commerce/static/phones/touch"
    # print('Scraping Dynamic Content - Load Button')
    # xPathScraper = XPathScraper(url=loadbybutton)
    # xPathScraper.scrapeXPATH_DynamicLoadButton(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfLoadMoreElement="//div/a[text()='More']",\
    #             xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")
    
    # print('Scraping Dynamic Content - Scroll to Load')
    # xPathScraper = XPathScraper(url=loadbyscrolling)
    # xPathScraper.scrapeXPATH_DynamicScroll(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")

    # print('Scraping Dynamic Content - Pagination')
    # xPathScraper = XPathScraper(url=loadbypagination)
    # xPathScraper.scrapeXPATH_DynamicPagination(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfPaginationElement="//div[@id='static-pagination']/nav/ul[@class='pagination']/li/a[@rel='next']",\
    #             xPathOfElementToScrape="//div[contains(@class, 'thumbnail')]",\
    #                 xPathOther=["//h4[@class='price float-end card-title pull-right']"])
    
    # bbcShopPagination="https://shop.bbc.com/collections/merchandise"
    # print('Scraping Dynamic Content - Pagination')
    # xPathScraper=XPathScraper(url=bbcShopPagination)
    # xPathScraper.scrapeXPATH_DynamicPagination(\
    #     xPathOfPresenceElement="//div[@id='bc-sf-filter-products']", \
    #         xPathOfPaginationElement="//div[@id='bc-sf-filter-bottom-pagination']/ul/li/a[text()='→']", \
    #             xPathOfElementToScrape="//div[contains(@class,'bc-sf-filter-product-item-inner')]",\
    #                 xPathOther=["//a[@class='bc-sf-filter-product-item-title']","//p[@class='bc-sf-filter-product-item-price']/span[@class='bc-sf-filter-product-item-sale-price']"])
    # xPathScraper._quitDriver()
    
    # print('Scraping Dynamic Content - Load Button')
    # bsScraper = BeautifulSoupScraper(url=loadbybutton)
    
    # elementsToScrape:dict[str,str]={"h4":"price float-end card-title pull-right", "a":"title"}
    # bsScraper.scrapeBeautifulSoup_DynamicLoadButton(\
    #     presenceElementCSS="a.ecomerce-items-scroll-more",\
    #         elementsToScrape=elementsToScrape)
    
    # print('Scraping Dynamic Content - Load by Scroll')
    # bsScraper = BeautifulSoupScraper(url=loadbyscrolling)
    # elementsToScrape:dict[str,str]={"h4":"price float-end card-title pull-right", "a":"title"}
    
    # bsScraper.scrapeBeautifulSoup_DynamicScroll(presenceElementCSS="div.row.ecomerce-items.ecomerce-items-scroll",\
    #     elementsToScrape=elementsToScrape)
    print('Scraping Dynamic Content - Load by Pagination')
    bsScraper = BeautifulSoupScraper(url=loadbypagination)
    elementsToScrape:dict[str,str]={"h4":"price float-end card-title pull-right", "a":"title"}
    
    bsScraper.scrapeBeautifulSoup_DynamicPagination(presenceElementCSS="a[rel='next']",\
        elementsToScrape=elementsToScrape)
    
    bsScraper._quitDriver()


if __name__ == "__main__":
    main()