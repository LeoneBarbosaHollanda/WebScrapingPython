from lib2to3.pgen2 import driver
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
#navegador.fullscreen_window()
sleep(5)
tabela = {'nome': [], 'marca': [], 'preco': []}
#navegador.execute_script("document.body.style.zoom='25%'")
cont = len(respostas)
print(respostas)
j=0
o=500
for i, d in enumerate(respostas):
    nome = d.find('h2').get_text()
    marca = d.find('h3').get_text()
    preco = d.find('h4').get_text()

    if nome not in tabela['nome'] or marca not in tabela['marca'] or preco not in tabela['preco']:

        sleep(2)
        # navegador.execute_script("document.body.style.zoom='25%'")
        
            
        tabela['nome'].append(nome)
        tabela['marca'].append(marca)
        tabela['preco'].append(preco)
        while True:
            try:
                navegador.find_element(
            By.XPATH, f'//*[@id="crsl-feat-slide0{i+1}"]/div/a').click()
            except:
                try:
                    navegador.find_element(
                By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a').click()
                except:
                    navegador.execute_script(f"window.scrollTo({j},{o});")
                    j=o
                    o+=500
            else:
                break
        
        
        sleep(2)
        navegador.back()
        
        sleep(2)
        print(f'conseguiu pegar {i+1}')
    
# print(tabela)
tab = pd.DataFrame(tabela)
print(tab)
