import requests
from bs4 import BeautifulSoup

url: str = "https://new-science.ru/category/news/page/2/"
response = requests.get(url)

# /// Через BeautifulSoup решение
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

# /// Альтернативное решение
title_start_index = response.text.find("<title>")
title_end_index = response.text.find("</title>")
print(f"Старт: {title_start_index}\nКонец: {title_end_index}")
print(f"{response.text[title_start_index:title_end_index]}")



with open("site.html", mode="w", encoding="utf-8") as file:
    file.write(response.text)
