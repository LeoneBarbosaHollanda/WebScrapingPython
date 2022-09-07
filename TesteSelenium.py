from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.vipleiloes.com.br/')
sleep(5)
navegador.find_element(
    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/div[4]/div/div/div[2]/div/div[1]').click()
navegador.find_element(
    By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a/img').click()
