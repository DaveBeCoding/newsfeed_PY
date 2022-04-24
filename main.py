from utili.scrapes import Scraper

def main():
    print("Hello Test scraper")
    Scraper('https://www.coindesk.com', 'display-desktop-none').test_funct()


main()


# Found the URL 2: https://www.coindesk.com/consensus2022/
# python main.py | grep -- https