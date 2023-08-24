from bs4 import BeautifulSoup
import requests

def credit_repair():
    url = 'https://www.consumeraffairs.com/finance/credit-repair/'
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    
    h2_elements = soup.find_all("h2", class_="ca-h2")

    for h2 in h2_elements:
       
        print(h2.text)

        
        next_sibling = h2.find_next_sibling()
        if next_sibling:
            print(next_sibling.text.strip())

credit_repair()
