from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

HEADERS ={
    'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/116.0.0.0 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

def scrapeConsumerAffairs(url = 'https://www.consumeraffairs.com/finance/banks.htm'):
    response = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(response.text, 'html.parser')
    banks = soup.findAll("a", attrs={"class":"ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer"})

    return [bank.text for bank in banks]


