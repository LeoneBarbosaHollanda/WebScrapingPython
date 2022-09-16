from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"
}
url ='https://www.vipleiloes.com.br/'

options = Options
servico = Service(ChromeDriverManager().install())
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find("div", class_="card crd-main d-flex")
navegador = webdriver.Chrome(service=servico)
navegador.get(url)
navegador.maximize_window()
timeout=30
for j,d in enumerate(respostas):
    try:
        WebDriverWait(navegador, timeout).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='sidebar-menu-container']/div[2]/div[4]/div/div/div[2]/div/div[1]"))).click()
        
    except:
        print('deu certo nao, otario')