
from lib2to3.pgen2.token import OP
from logging import exception
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sopa(url):
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup


#options.add_argument(' --headless')
headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
urlMain = 'https://www.vipleiloes.com.br/'

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get(urlMain)
navegador.maximize_window()
soup = sopa(urlMain)
# print(navegador)
respostas = soup.find_all("a", class_='hm-catitem')


#print(respostas )


for k, j in enumerate(respostas):
    PgAnt = 1
    PgPrx = 1
    numPg = 1
    urlPag = f"{urlMain}{j['href']}"
    navegador.find_element(
        By.XPATH, f'//*[@id="sidebar-menu-container"]/div[2]/div[3]/div/div/a[{k+1}]').click()
    soup = sopa(urlPag)
    siteCarros = soup.find_all('div', class_='itm-card')

    for l, v in enumerate(siteCarros):
        pag = v.find('a', attrs={'class': 'itm-cdlink'})['href']
        pag = pag.replace(f'Pagina={PgAnt}', f'Pagina={PgPrx}')
        urlCarro = f'{urlMain}{pag}'
        try:
            navegador.find_element(
                By.XPATH, f'//*[@id="cardmode"]/div/div[{l+1}]').click()

        except Exception:
            try:
                car = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(
                    (By.XPATH, f'//*[@id="listing-cars"]/div[2]/div/div[1]/div[2]/a[{numPg}]')))
                navegador.execute_script('arguments[0].click()', car)
                numPg += 1
                l = 0
                PgAnt = PgPrx
                PgPrx += 1
                print('o L é'+l)
            except Exception:
                navegador.find_element(
                    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a').click()

                break
        else:
            navegador.back()


#tabela = {'nome': [], 'marca': [], 'preco': []}
# navegador.execute_script("document.body.style.zoom='25%'")
