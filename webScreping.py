from wsgiref import headers
import Url
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"}
while True:
    Carros = str(input("""Escola o modelo do carro no Site de leiloes:
Ford
Chevrolet
Suzuki
Porshe""")).lower()
    try:
        Carros = Url.urlCarros(Carros)
    except:
        print("ERRO!!!!!!\033[0:31:41M")
        print("Digite o nome do carro novamente")
    else:
        break
