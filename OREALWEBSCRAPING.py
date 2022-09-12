
from lib2to3.pgen2.token import OP
import site
from telnetlib import Telnet
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

def dados(classe):
    classe.find

options = Options()
#options.add_argument(' --headless')

url = 'https://www.vipleiloes.com.br/'

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)
navegador.get(url)
sleep(2)
navegador.maximize_window()
sleep(5)
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find_all("div", class_='card crd-main d-flex')

#sleep(5)
#tabela = {'Veiculo': [], 'Cor': [], 'Valor Fipe': [],'ano':[],'Combustivel':[],'Km rodada':[],'Localização do lote':[],'Situaçao de entrada':[],'Final Placa':[],'Comiteente':[]}
#navegador.execute_script("document.body.style.zoom='25%'")
#cont = len(respostas)
print(respostas)
scrollmin=0
scrollmax=500
while True:
    for j,d in enumerate(respostas):
        urlCarro = d.find('a').get_text()
        #parei aqui tentando pegar a URL
        
        for k in range(0,3):
            navegador.find_element(By.XPATH,'//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[3]/a/i')
             
        #sleep(5)
        try:
            #Tenta clicar no carro
            navegador.find_element(By.XPATH,f'//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[{j+1}]').click()
            sleep(5)
        except Exception:
                #Se ele nao clicar no carro, ele desce
                navegador.execute_script(f'window.scrollTo({scrollmin},{scrollmax});')
                scrollmin=scrollmax
                scrollmax+=500
                navegador.find_element(By.XPATH,f'//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[{j+1}]').click()
        
        #se ele clicar no carro, ele vai retornar 
        navegador.back()
        sleep(5)
    
            
    