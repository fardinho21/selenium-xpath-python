from BaseScraper import BaseScraper


def main():
    loadbyscrolling="https://webscraper.io/test-sites/e-commerce/scroll/phones/touch"
    loadbybutton="https://webscraper.io/test-sites/e-commerce/more/phones/touch"
    baseScraper = BaseScraper(url=loadbyscrolling, dynamicSite=True)
    baseScraper.scrapeXPATH_Dynamic(loaderType="scroll")
    baseScraper._quitDriver()
    pass


if __name__ == "__main__":
    main()