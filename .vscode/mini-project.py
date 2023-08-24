import requests
from bs4 import BeautifulSoup
import csv


# set up the html parser from the package
# page = ""
page_to_scrape = requests.get("http://books.toscrape.com/catalogue/category/books/young-adult_21/page-1.html")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#scrape from quotes, include the author
prices = soup.findAll("p", attrs={"price_color":"text"})
titles = soup.findAll("span", attrs={"class":"text"})
