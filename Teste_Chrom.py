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
url ='https://www.leilomaster.com.br/veiculos?dados.VEI_TIPO.keyword=Categoria%3A%20Ve%C3%ADculos%7CVe%C3%ADculos'

options = Options
servico = Service(ChromeDriverManager().install())
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find("div", class_="col-12 col-md-12 col-lg-12 q-mb-sm")
navegador = webdriver.Chrome(service=servico)
navegador.get(url)
print(respostas)
sleep(10)