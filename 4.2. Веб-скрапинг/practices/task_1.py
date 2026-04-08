import requests

url: str = "https://new-science.ru/category/news/page/2/"
response = requests.get(url)
print(
    "Длина текста {}\nПервые 500 символов:\n{}".format(
        len(response.text), response.text[:500]
    )
)

with open("site.html", mode="w", encoding="utf-8") as file:
    file.write(response.text)
