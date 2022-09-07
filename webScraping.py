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


options = Options()
#options.add_argument(' --headless')
options.add_argument('window-size=1980,1080')
url = 'https://www.vipleiloes.com.br/'

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
# navegador.execute_script('document.body.style.zoom="25%"')

# navegador.execute_script('document.body.style.zoom="25%"')
sleep(10)

#kmRodada = soup.find("div", class_='crd-linefour').get_text()
tabela = {'nome': [], 'marca': [], 'preco': []}
for i, d in enumerate(respostas):
    nome = d.find('h2').get_text()
    marca = d.find('h3').get_text()
    preco = d.find('h4').get_text()

    if nome in tabela['nome'] and marca in tabela['marca'] and preco in tabela['preco']:
        pass
    else:
        tabela['nome'].append(nome)
        tabela['marca'].append(marca)
        tabela['preco'].append(preco)
        navegador.find_element(
            By.XPATH, f'//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[{1+i}]').click()
        sleep(0.5)
        navegador.find_element(
            By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a/img').click()
        sleep(0.5)
        print(f'conseguiu pegar {i+1}')
        if i > 6:
            navegador.find_element(
                By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
            if i > 10:
                navegador.find_element(
                    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
                if i > 14:
                    navegador.find_element(
                        By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
                    if i > 18:
                        navegador.find_element(
                            By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
                        if i > 22:
                            navegador.find_element(
                                By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
                            if i > 26:
                                navegador.find_element(
                                    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()


# print(tabela)
tab = pd.DataFrame(tabela)
print(tab)
