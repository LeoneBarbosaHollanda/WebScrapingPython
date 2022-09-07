import site
import pandas as pd
import json
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.kabum.com.br/busca/cadeiras'


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find(
    "div", class_='sc-3b515ca1-0 djGoHl availablePricesCard')
# print(soup)
# print(site)
print(respostas.get_text())
