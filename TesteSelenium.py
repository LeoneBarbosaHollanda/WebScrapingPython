from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import OP

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.vipleiloes.com.br/')
sleep(5)
navegador.execute_script("window.scrollTo(0,1000);")
sleep(5)
navegador.find_element(
    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[1]/a').click()
sleep(5)
navegador.back()
print('ate aqui prestou')
sleep(20)
'''navegador.find_element(
    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[1]').click()
sleep(10)'''

#new_height = navegador.execute_script("return document.body.scrollHeight")
