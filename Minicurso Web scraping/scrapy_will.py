import requests
from bs4 import BeautifulSoup

url = "https://pt.tradingeconomics.com/forecast/commodity"

page = requests.get(url)

sopa = BeautifulSoup(page.text, "html.parser")

# tabelaPrincipal = sopa.find_all("div", class_="table-responsive")

comoditiesTag = sopa.find_all("b")
precosTag = sopa.find_all(id="p", class_="datatable-item")

comodities = [comoditie.get_text() for comoditie in comoditiesTag]
pLimpo = [preco.get_text().strip() for preco in precosTag]

with open("comodities.csv", "w") as file:
    for i in range(len(comodities)):
        file.write(comodities[i]+","+pLimpo[i]+"\n")

