import requests
from bs4 import BeautifulSoup as bs


url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

print(page)

print(page.status_code)

print(page.text)
print()
print(page.content)

sopa = bs(page.text, "html.parser")

print(sopa.prettify())
print()

print(sopa.find_all("p"))

print()

print(sopa.find_all("p")[2].get_text())
print()

print(sopa.find_all(class_="chorus"))

print()

print(sopa.find_all("p", class_="chorus"))
print()
print(sopa.find_all(id="third"))
print("\nFim")
