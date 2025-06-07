from BaseScraper import BaseScraper


def main():
    
    loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    # print('Scraping Dynamic Content - Load Button')
    # baseScraper = BaseScraper(url=loadbybutton)
    # baseScraper.scrapeXPATH_DynamicLoadButton(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfLoadMoreElement="//div/a[text()='More']",\
    #             xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")
    
    loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    # print('Scraping Dynamic Content - Scroll to Load')
    # baseScraper = BaseScraper(url=loadbyscrolling)
    # baseScraper.scrapeXPATH_DynamicScroll(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfElementToScrape=".//h4[@class='price float-end pull-right']")

    loadbypagination="https://webscraper.io/test-sites/e-commerce/static/phones/touch"
    # print('Scraping Dynamic Content - Pagination')
    # baseScraper = BaseScraper(url=loadbypagination)
    # baseScraper.scrapeXPATH_DynamicPagination(\
    #     xPathOfPresenceElement="//div[contains(@class, 'thumbnail')]",\
    #         xPathOfPaginationElement="//div[@id='static-pagination']/nav/ul[@class='pagination']/li/a[@rel='next']",\
    #             xPathOfElementToScrape="//div[contains(@class, 'thumbnail')]",\
    #                 xPathOther=["//h4[@class='price float-end card-title pull-right']"])
    
    bbcShopPagination="https://shop.bbc.com/collections/merchandise"
    print('Scraping Dynamic Content - Pagination')
    baseScraper=BaseScraper(url=bbcShopPagination)
    baseScraper.scrapeXPATH_DynamicPagination(\
        xPathOfPresenceElement="//div[@id='bc-sf-filter-products']", \
            xPathOfPaginationElement="//div[@id='bc-sf-filter-bottom-pagination']/ul/li/a[text()='→']", \
                xPathOfElementToScrape="//div[contains(@class,'bc-sf-filter-product-item-inner')]",\
                    xPathOther=["//a[@class='bc-sf-filter-product-item-title']","//p[@class='bc-sf-filter-product-item-price']/span[@class='bc-sf-filter-product-item-sale-price']"])
    baseScraper._quitDriver()


if __name__ == "__main__":
    main()