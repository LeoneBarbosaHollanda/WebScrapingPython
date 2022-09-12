
from lib2to3.pgen2.token import OP
import site
import pandas as pd
import json
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
#options.add_argument(' --headless')

url = 'https://www.vipleiloes.com.br/Veiculos/ListarVeiculos?EstadoGeral=2'

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
navegador.get(url)
sleep(5)
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find_all("div", class_='itm-card')
#navegador.fullscreen_window()
sleep(5)
#tabela = {'nome': [], 'marca': [], 'preco': []}
#navegador.execute_script("document.body.style.zoom='25%'")
cont = len(respostas)
print(respostas)




