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


def clickMais(i, Quant):
    if i > Quant:
        navegador.find_element(
            By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
        navegador.execute_script("window.scrollTo(0,1500);")


options = Options()
#options.add_argument(' --headless')
options.add_argument('window-size=1600,2000')
url = 'https://www.vipleiloes.com.br'

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"
}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find_all("div", class_='card crd-main d-flex')
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
navegador.get(url)
element = navegador.find_element(By.TAG_NAME, 'body')
tabela = {'nome': [], 'marca': [], 'preco': []}
cont = len(respostas)
for i, d in enumerate(respostas):
    nome = d.find('h2').get_text()
    marca = d.find('h3').get_text()
    preco = d.find('h4').get_text()

    if nome not in tabela['nome'] and marca not in tabela['marca'] and preco not in tabela['preco']:
        print('prestou')
        sleep(2)
        for i in range(0, 12):
            print(f"prestou {i}vezes")
            sleep(0.5)
            element.send_keys(Keys.PAGE_DOWN)
        tabela['nome'].append(nome)
        tabela['marca'].append(marca)
        tabela['preco'].append(preco)
        navegador.find_element(
            By.XPATH, f'//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[{i+1}]/a/img').click()

        navegador.find_element(
            By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a/img').click()

        print(f'conseguiu pegar {i+1}')
        clickMais(i, 6)
        clickMais(i, 10)
        clickMais(i, 14)
        clickMais(i, 18)
        clickMais(i, 22)

        #clickMais(i, 26)
    if i+1/2 == cont:
        break
# print(tabela)
tab = pd.DataFrame(tabela)
print(tab)
