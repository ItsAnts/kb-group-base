import requests
from bs4 import BeautifulSoup

url: str = "https://new-science.ru/"

response = requests.get(url=url)
text: str = response.text

soup = BeautifulSoup(text, "html.parser")
links = soup.find_all("a")
save: str = ""
for index in range(len(links)):
    save = save + str(links[index]) + "\n"
with open("links.txt", mode="w", encoding="utf-8") as file:
    file.write(save)
