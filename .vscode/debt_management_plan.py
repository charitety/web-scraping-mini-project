import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.consumeraffairs.com/finance/debt-management-plans/#compare-top-picks"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def scrape_data(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    
    plan_class_name = "brnd-crd-v2__ttl"
    title_elements = soup.find_all('h3', class_=plan_class_name)
    
    plan_titles = []
    for title_element in title_elements:
        plan_title = title_element.get_text().strip()
        plan_titles.append(plan_title)
    
    program_length_elements = soup.find("dd", class_="tp-pcks-brd-crd__itm-val")
    program_length = program_length_elements.get_text().strip()
    
    monthly_fee_elements = soup.find("dd", class_="tp-pcks-brd-crd__itm-val")
    monthly_fee = monthly_fee_elements.get_text().strip()
    
    debt_minimum_elements = soup.find("dd", class_="tp-pcks-brd-crd__itm-val")
    debt_minimum = debt_minimum_elements.get_text().strip()
    
    reviews_element = soup.find(class_="ca-btn ca-btn--body-fs dynmc-tb__btn")
    reviews = reviews_element.get_text().strip()
    
    return plan_titles, program_length, monthly_fee, debt_minimum, reviews

# Call the scrape_data function
plan_titles, program_length, monthly_fee, debt_minimum, reviews = scrape_data(url)

# Print the scraped data
print("Scraped Data:")
for i in range(len(plan_titles)):
    print("Plan Title:", plan_titles[i])
    print("Program Length:", program_length)
    print("Monthly Fee:", monthly_fee)
    print("Debt Minimum:", debt_minimum)
    print("Reviews:", reviews)
    print("\n")

# Write the data to a CSV file
csv_filename = "scraped_data.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Plan Title", "Program Length", "Monthly Fee", "Debt Minimum", "Reviews"])
    for title in plan_titles:
        writer.writerow([title, program_length, monthly_fee, debt_minimum, reviews])

print("Data has been written to", csv_filename)
