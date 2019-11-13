## web scraping modularizado
import requests as rq
from bs4 import BeautifulSoup as bs


url = "https://www.hobolink.com/p/b9b44681781bf78c9c6e1382637ee8ff"

page = rq.get(url)

# print(page.status_code)
## isso mostra se a conexão foi bem sucedida

sopa = bs(page.text, "html.parser")

# fatores = sopa.find_all("span", class_="latest-conditions-info-label")
fatores = sopa.find_all("div", class_="latest-conditions-info")

nomeFat = sopa.find_all("div", class_="latest-conditions-info-label")
valores = sopa.find_all("span", class_="latest-conditions-info-reading")
unidades = sopa.find_all("span", class_="latest-conditions-info-units")

