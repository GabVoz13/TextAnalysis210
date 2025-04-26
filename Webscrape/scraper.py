import requests
from bs4 import BeautifulSoup

url = 'http://www.textfiles.com/directory.html'  # You can change this later if you want

response = requests.get(url)

if response.status_code == 200:
    print("Page downloaded successfully!")
else:
    print("Failed to download page:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    href = link.get('href')
    text = link.text
    print(f"Text: {text} -> Link: {href}")

with open('scraped_links.txt', 'w', encoding='utf-8') as f:
    for link in links:
        href = link.get('href')
        text = link.text
        f.write(f"Text: {text} -> Link: {href}\n")
