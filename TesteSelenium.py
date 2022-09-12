import enum
from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import OP

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"
}
options = Options
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
url = 'https://www.leilomaster.com.br/veiculos?dados.VEI_TIPO.keyword=Categoria%3A+Ve%C3%ADculos%7CVe%C3%ADculos'
navegador.get(url)

#navegador.execute_script("window.scrollTo(0,1000);")
sleep(2)

k=0
o=500
while True:
    for j,d in enumerate(respostas):
        try:
            navegador.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div[1]/i')
        except  Exception:
            print("Sem anuncio para fechar")
        sleep(5)
        try:
            #Tenta clicar no 
            navegador.find_element(By.XPATH,f'//*[@id="q-app"]/div/div[2]/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[{j+1}]').click()
            sleep(5)
        except Exception:
            navegador.execute_script(f'window.scrollTo({k},{o}')
            k=o
            o+=500
        else:
            navegador.back()
            sleep(5)
        if j+1==60:
            navegador.find_element('')
            url = f''
    

