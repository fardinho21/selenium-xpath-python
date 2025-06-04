from BaseScraper import BaseScraper


def main():
    baseScraper = BaseScraper(url="https://webscraper.io/test-sites/e-commerce/more/phones/touch", dynamicSite=True)
    baseScraper.scrapeXPATH_Dynamic(xPath="")
    baseScraper._quitDriver()
    pass


if __name__ == "__main__":
    main()