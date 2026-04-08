import requests
from bs4 import BeautifulSoup

url: str = "https://new-science.ru"

response = requests.get(url=url)
text = response.text

soup = BeautifulSoup(text, "html.parser")
posts = soup.find_all('h2')
titles: str = ""
for post in posts:
    title = post.a
    if title:
        titles = titles + title.text + "\n"

with open("titles.txt", mode="w", encoding="utf-8") as file:
    file.write(titles)