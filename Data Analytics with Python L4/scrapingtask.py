import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Request the webpage
url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
response.raise_for_status()  # check for errors

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'lxml')

# Step 3: Find all data containers
countries = soup.find_all('div', class_='country')

# Step 4: Extract the required data
data = []
for country in countries:
    name = country.find('h3', class_='country-name').text.strip()
    capital = country.find('span', class_='country-capital').text.strip()
    population = country.find('span', class_='country-population').text.strip()
    area = country.find('span', class_='country-area').text.strip()
    data.append({
        'Name': name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

# Step 5: Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv('countries.csv', index=False)
print("Data saved to countries.csv")
