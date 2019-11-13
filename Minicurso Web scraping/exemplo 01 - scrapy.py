# AUTOR: GABRIEL DANTAS
# --------------------
# ------SCRIPT--------
# ÚTIL PARA VERIFICAR INFORMAÇÕES EM VÁRIOS SITES DIFERENTAS.
# NO TUTORIAL IREMOS ENTRAR EM UM SITE E PEGAR O PREÇO DA SOJA
# EM TEMPO REAL, ALÉM DISSO CRIAR UM ALERTA BÁSICO QUANDO O PREÇO
# ESTIVER ALTO.



#IMPORTANMOS AS BIBLIOTECAS NECESSÁRIAS
import urllib.request as rq #SERVE PARA 'ENTRAR' EM SITES E OBTER SEU CONTEÚDO

#URL DO SITE QUE DEVE SER ANALISADO
url = 'https://pt.tradingeconomics.com/forecast/commodity'

#A VARIÁVEL SITE RECEBE UMA CLASSE HTTPResponse (CODIFICADAS)
site = rq.urlopen(url)

#LEMOS E DECODIFICAMOS AS INFORMAÇÕES
site_analisado = site.read().decode('UTF-8')

#PROCURAMOS PELA INFORMÇÃO 'SOJA', A FUNÇÃO .find() RETORNA O NÚMERO
#DA POSIÇÃO EM QUE A PRIMEIRA LETRA DA PALAVRA PROCURADA SE ENCONTRA
# E SALVAMOS ESSE NÚMERO NA VAR inicio.
inicio = site_analisado.find('Soja')

#VERIFICAMOS ONDE O VALOR DE SOJA SE ENCONTRA (POSIÇÃO)
# E ACRESCENTAMOS MAIS 258.
inicio = inicio + 258

#SABEMOS QUE O VALOR É COMPOSTO POR 8 ESPAÇOS, ENTÃO ADICIOMOS MAIS 8
#NA VAR fim.
fim = inicio + 8

#FAZEMOS O FATIAMENTO COM DO INICIO AO FIM E SALVAMOS NA VAR p_soja
#(preço da soja)
p_soja = site_analisado[inicio:fim]

#CONVERTEMOS O VALOR DE p_soja  DE string  PARA float.
p_soja = float(p_soja)

#PEDIMOS PARA MOSTRAR O VALOR ATUAL
#print('O valor da soja atual é: ', p_soja)

#PEDIMOS PARA MOSTRAR COM MAIS ESTILO
print(f'O preço atual da soja é R$ {p_soja}')



