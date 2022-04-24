from bs4 import BeautifulSoup
import requests


class Scraper:
    # def __init__(self, name):
    #     self.name = name

    def say_hi(self):
        print('Hello, from tester')

    def test_funct(self):
        # user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

        # url = 'https://stackoverflow.com/questions/tagged/python'
        url = 'https://www.coindesk.com'

        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, 'html.parser')
        tables = soup.find_all('h3', {'class' : 'typography__StyledTypography-owin6q-0'})
        print(tables)       
        # class="typography__StyledTypography-owin6q-0 eFJWyp redirect-tag"
        
        # count = 0
        # for a in soup.find_all('h3', {'class' : 'typography__StyledTypography-owin6q-0'}):
        #     count = 1 + count
        #     print(f'Found the URL {count}:', a['href'])

    def scraping(self):
        # pass
        # This example uses Python 2.7 and the python-request library.

        from requests import Request, Session
        from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
        import json

        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            print(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def main():
        p1 = Scraper("john")
        p1.say_hi()
        p1.scraping()


if __name__ == '__main__':
    Scraper.main()
