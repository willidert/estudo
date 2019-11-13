import requests
from bs4 import BeautifulSoup

url = "https://pt.tradingeconomics.com/forecast/commodity"

page = requests.get(url)

sopa = BeautifulSoup(page.text, "html.parser")

tabelaPrincipal = sopa.find_all("div", class_="table-responsive")

for tabela in tabelaPrincipal:
    elemento = tabela.find_all("tr")
    for produto in elemento:
        if produto.find("b") != None:
            mercadoria = produto.find("b").get_text()
            valor = produto.find(id="p", class_="datatable-item").get_text().strip()
            print(mercadoria+" = "+valor)

