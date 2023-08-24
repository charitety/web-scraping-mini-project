import requests
from bs4 import BeautifulSoup

url = "https://www.consumeraffairs.com/finance/debt-management-plans/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

def scrape_data(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    planTitle = soup.find(class_="brnd-crd-v2__ttl").get_text()
    programLength = soup.find(class_="tp-pcks-brd-crd__itm-val").get_text()
    monthlyFee = soup.find(class_="tp-pcks-brd-crd__itm-val").get_text()
    debtMinimum = soup.find(class_="dynmc-tb__cell-ftr").get_text()
    reviews = soup.find(class_="ca-btn ca-btn--body-fs dynmc-tb__btn").get_text()

    return {
        "Plan Title": planTitle,
        "Program Length": programLength,
        "Monthly Fee": monthlyFee,
        "Debt Minimum": debtMinimum,
        "Reviews": reviews
    }

data = scrape_data(url)

print("Plan Title:", data["Plan Title"])
print("Program Length:", data["Program Length"])
print("Monthly Fee:", data["Monthly Fee"])
print("Debt Minimum:", data["Debt Minimum"])
print("Reviews:", data["Reviews"])
