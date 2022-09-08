from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.vipleiloes.com.br/')
element = navegador.find_element(By.TAG_NAME, 'body')
element.send_keys(Keys.PAGE_DOWN)
'''navegador.find_element(
    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[1]').click()
sleep(10)'''

#new_height = navegador.execute_script("return document.body.scrollHeight")
