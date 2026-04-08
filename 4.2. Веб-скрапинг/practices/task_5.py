import requests
from bs4 import BeautifulSoup

url: str = "https://quotes.toscrape.com/"
response = requests.get(url=url)
text = response.text

# Цитаты и авторов
soup = BeautifulSoup(text, "html.parser")
divs = soup.find_all("div")
print(text)
for div in divs:
    spans = div.find_all("span")
    if len(spans) == 2:
        print(f"Цитата: {spans[0].text}\nАвтор: {spans[1].text}")