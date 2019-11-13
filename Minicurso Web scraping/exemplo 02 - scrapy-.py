# AUTOR: GABRIEL DANTAS
# --------------------
# ------SCRIPT--------
# ÚTIL PARA VERIFICAR INFORMAÇÕES EM VÁRIOS SITES DIFERENTAS.
# NO TUTORIAL IREMOS ENTRAR EM UM SITE E PEGAR O PREÇO DA SOJA
# EM TEMPO REAL, ALÉM DISSO CRIAR UM ALERTA BÁSICO QUANDO O PREÇO
# ESTIVER ALTO.



#IMPORTANMOS AS BIBLIOTECAS NECESSÁRIAS
import urllib.request as rq #SERVE PARA 'ENTRAR' EM SITES E OBTER SEU CONTEÚDO
from time import sleep as espere #IMPORTAMOS A FUNÇÃO SLEEP E CHAMAMOS ELA DE
                                 #espere

import os

# CRIAMOS UMA FUNCÇÃO E COLOCAMOS TODOS OS CÓDIGO DENTRO DELA:
url = 'https://pt.tradingeconomics.com/forecast/commodity'
def preco_atual():
    site = rq.urlopen(url)
    site_analisado = site.read().decode('UTF-8')
    inicio = site_analisado.find('Soja')
    inicio = inicio + 258
    fim = inicio + 8
    p_soja = site_analisado[inicio:fim]
    p_soja = float(p_soja)
    os.system('cls')
    print(f'O preço atual da soja é R$ {p_soja}')
    return p_soja
    
    
if __name__ == '__main__':
    while True:
        preco_atual()
        espere(10)
