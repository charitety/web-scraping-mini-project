import requests, csv
from bs4 import BeautifulSoup
import pandas as pd


page_scrape = requests.get("https://www.consumeraffairs.com/finance/auto-loans/#featured-all")
soup = BeautifulSoup(page_scrape.text, "html.parser")

# print(soup.prettify())

names = soup.findAll("div", attrs={"class": "brd-card__tit-innr"})
# descriptions = soup.findAll("p", attrs={"class": "brd-card__desc brd-card__td h-coll-vert ca-txt-bd-2  brd-card__desc--del"})
# descriptions = soup.find_all('div', class_='rvw-bd')


top_pick_names = soup.findAll("strong", attrs={"class": "sngl-brnd-crd__nm"})

top_pick_desc = soup.findAll("ul", attrs={"class": "sngl-brnd-crd__lst"})


for top in top_pick_names:
    print(top.text)


for top_desc in top_pick_desc:
    print(top_desc.text)

# file = open('export_data.csv', 'w', newline='')

# for name in names:
#     print(name.text)

# for description in descriptions:
#     print(description.text)

    # company_names = []
    #
    # for i in range(0, len(names)):
    #     company_names += names[i]
    #     print(company_names)

# writer = csv.writer(file)

    file = open('export_data.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ([top_pick_names, top_pick_desc])
    writer.writerow(headers)
    file.close()





data = pd.read_csv('export_data.csv')
data.head()


# top_pics = soup.findAll("strong", attrs={"class": "sngl-brnd-crd__nm"})