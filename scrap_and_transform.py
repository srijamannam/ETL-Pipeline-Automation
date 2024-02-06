from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd

# Define a list of URLs
urls = [
    'https://www.zalando.it/tommy-jeans-basket-sneakers-basse-brown-tob12o06k-o11.html',
    'https://www.zalando.it/puma-ca-pro-fs-unisex-sneakers-basse-puma-whitemyrtle-pu115o0jm-a16.html',
    'https://www.zalando.it/diadora-winner-unisex-sneakers-basse-whitehigh-rise-d2915o03m-a12.html',
    'https://www.zalando.it/hummel-marathona-reach-lx-unisex-sneakers-basse-black-magnet-hu315o03o-c11.html'
]

# Create a CSV file and write the header
header = ['Brand', 'Name', 'Price', 'Date']
with open('shoes_db.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

def scrape_and_append_data(url):
    page = requests.get(url, verify= True)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract the data
    brand = soup.find("h3", class_="FtrEr_ QdlUSH FxZV-M HlZ_Tf _5Yd-hZ").text.strip()
    name = soup.find("span", class_="EKabf7 R_QwOV").text.strip()
    try:
        price = soup.find("span", class_="sDq_FX _4sa1cA dgII7d Km7l2y").text.strip()
    except AttributeError:
        price = soup.find("span", class_="sDq_FX _4sa1cA FxZV-M HlZ_Tf").text.strip()
    today = datetime.date.today()

    data = [brand, name, price, today]

    # Append data to the CSV file
    with open('shoes_db.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Process all the URLs
for url in urls:
    scrape_and_append_data(url)


# Read the CSV file and print the DataFrame
df = pd.read_csv('shoes_db.csv')

# Perform the 'Price' column modifications
df['Price'] = df['Price'].str.replace(r'[^\d,.]', '', regex=True)
df['Price'] = df['Price'].str.replace(',', '.', regex=True).astype(float)

df.to_csv('shoes_db.csv', index=False)
# Display the modified DataFrame
print(df)
