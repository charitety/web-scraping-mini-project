import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define the URL for the category you want to scrape
import requests
from bs4 import BeautifulSoup

base_url = "https://www.consumeraffairs.com"
category_url = "https://www.consumeraffairs.com/finance/debt-management-plans/"

def download_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def extract_data(page_content):
    soup = BeautifulSoup(page_content, "html.parser")

    # Extracting rating
    rating_element = soup.find("div", class_="text")
    rating = rating_element.get_text() if rating_element else None

    # Extracting other data
    # Replace these placeholders with actual code to extract the required information

    # Extracting rating
    rating_element = soup.find("div", class_="text")
    rating = rating_element.get_text() if rating_element else None

    # Extracting companies considered
    companies_considered = []
    companies_considered_elements = soup.select(".considered-companies .company-name")
    for company_element in companies_considered_elements:
        companies_considered.append(company_element.get_text())

    # Extracting companies selected
    companies_selected = []
    companies_selected_elements = soup.select(".selected-companies .company-name")
    for company_element in companies_selected_elements:
        companies_selected.append(company_element.get_text())

    # Extracting reviews
    reviews = []
    review_elements = soup.select(".review-text")
    for review_element in review_elements:
        reviews.append(review_element.get_text())

    # Extracting features
    features = []
    features_elements = soup.select(".product-feature")
    for feature_element in features_elements:
        features.append(feature_element.get_text())

    # Return a dictionary containing the extracted data
    data = {
        "companies_considered": companies_considered,
        "companies_selected": companies_selected,
        "Rating": rating,
        "Reviews": reviews,
        "features": features
    }
    return data

# Download the page content
page_content = download_page(category_url)

if page_content:
    extracted_data = extract_data(page_content)
    print(extracted_data)
else:
    print("Failed to download the page.")


# def save_to_csv(data_list, file_name):
#     with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
#         fieldnames = ["Title", "Rating", "Reviews", "TollFreeNumber"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data_list)

# def main():
#     # Step 2: Download the category page
#     category_page = download_page(base_url + category_url)
#     if category_page:
#         # Step 3: Extract data from the downloaded page
#         data_list = []
#         data = extract_data(category_page)
#         data_list.append(data)
        
#         # Step 4: Save data to CSV
#         save_to_csv(data_list, "output.csv")
#     else:
#         print("Failed to download the page.")

# if __name__ == "__main__":
#     main()
