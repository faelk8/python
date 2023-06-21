
##############################################################################################################
# Pega a cotação do dolar e do euro atualizada
##############################################################################################################



import requests
import pandas as pd
from datetime import datetime
import time

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")
req_dic = requisicao.json()
cotacao_dolar = req_dic['USDBRL']['bid']
cotacao_euro = req_dic['EURBRL']['bid']

print(cotacao_dolar)
print(cotacao_euro)
