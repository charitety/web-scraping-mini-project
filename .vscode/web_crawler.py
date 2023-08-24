import requests
from bs4 import BeautifulSoup

class WebCrawler:
    def fetch_url(self, url):
        response = requests.get(url)
        return response

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all("div", attrs={"class": "tp-pcks-brd-crd__itm"})