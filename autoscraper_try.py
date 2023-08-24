import csv
import pandas as pd
from autoscraper import AutoScraper
import requests


url = "https://www.consumeraffairs.com/finance/auto-loans/#featured-all"
scraper = AutoScraper()


top5_list = ["Name of the Bank", "Description"]  # Replace with actual values


scraper.build(url, top5_list)
scraped_data = scraper.get_result_similar(url)


for bank in scraped_data:
    print(bank)


with open('export_data_auto.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(top5_list)
    writer.writerows(scraped_data)


df = pd.read_csv('export_data_auto.csv')

# Display the DataFrame
print(df.head())
