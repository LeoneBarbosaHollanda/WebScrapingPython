import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import mysql.connector

# conexao com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='main',

)

cursor = conexao.cursor()
# Verificar se existe ou nao uma tabela:
NomeTabela = str(input('Diga o nome da sua tabela: '))
cursor.execute('show tables')
Verificar = cursor.fetchall()
if (f'{NomeTabela}',) not in Verificar:
    print(f'Criando {NomeTabela}')

    cursor.execute(f'CREATE TABLE {NomeTabela} (id INT AUTO_INCREMENT PRIMARY KEY, preço VARCHAR(255),   Veículo VARCHAR(255),   Cor VARCHAR(255),   ValorFipe VARCHAR(255),   Ano VARCHAR(255),   Combustível VARCHAR(255), KM VARCHAR(255) ,SituaçãodeEntrada VARCHAR(255) ,FinalPlaca VARCHAR(255),  Comitente VARCHAR(255))')
    print('tabela criada com sucesso')
else:
    print('tabela ja criada')


def sopa(url):
    # receber os paramentro da url pra voltar os dados do site
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup


# headers do google pra baixar automaticamente sem precisar pesquisar no google
headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
# url da pagina principal
urlMain = 'https://www.vipleiloes.com.br/'
# no serviço ele baixa os headers necessario
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get(urlMain)
navegador.maximize_window()
soup = sopa(urlMain)
respostas = soup.find_all("a", class_='hm-catitem')
# lista que vai interagir do python pro banco de dados
listaBD = ['', '', '', '', '', '', '', '', '', '']
# a tabela que vai ficar cada dado do carro
tabela = {'preço': [], ' Veículo': [], ' Cor': [], ' Valor Fipe': [],  ' Ano': [],
          ' Combustível': [], ' KM': [], ' Situação de Entrada': [], ' Final Placa': [], ' Comitente': []}

x = 0
# durante a execuçao desse For, ele vai entrar em cada um dos sites, usados, seminovos e outros, e cada um deles o codigo vai pegar os dados
for k, j in enumerate(respostas):
    # aqui é pra pegar a url da prox pagina
    urlPag = f"{urlMain}{j['href']}"
    try:
        navegador.find_element(
            By.XPATH, f'//*[@id="sidebar-menu-container"]/div[2]/div[3]/div/div/a[{k+1}]').click()
    except:
        quit()
        exit()
    # Variaveis para ajudar a  pegas as paginas seguintes
    numPg = 2
    PgAnt = 1
    PgPrx = 2
    while True:
        # aqui ja dentro dos (semi novos) vai pegar os dados ate acabar TODOS os carros de todas as partes
        soup = sopa(urlPag)
        siteCarros = soup.find_all('div', class_='itm-card')
        contCarros = len(siteCarros)/2

        # entra no site do carro e pega os dados do carro
        for l, v in enumerate(siteCarros):
            if l > contCarros:
                break
            # usado pra pegar o preço pq nao tem dentro do site do carro, so fora
            pag = v.find('a', attrs={'class': 'itm-cdlink'})['href']
            tabela['preço'] = v.find('h3').get_text()
            listaBD[0] = tabela['preço']
            try:
                # aqui vai tentar clicar no carro, quando nao conseguir vai passar pra prox pagina(na linha 100)
                # quando esse TRY der certo, ele vai jogar todos os dados, colocar em um dicionario e no else(linha133) vai jogar para o banco de dados
                navegador.find_element(
                    By.XPATH, f'//*[@id="cardmode"]/div/div[{l+1}]').click()
                urlCarro = f'{urlMain}{pag}'
                soupDados = sopa(urlCarro)
                dados = soupDados.find('div', class_='col-md-12')
                carro = dados.find_all('p')
                quantBD = 1

                for j, d in enumerate(carro):
                    DadoCarros = d.get_text()
                    DadoCarros = DadoCarros.replace(
                        '\n', ' ').replace('  ', ' ').split(': ')

                    try:
                        tabela[f'{DadoCarros[0]}'].append(DadoCarros[1])
                        listaBD[quantBD] = DadoCarros[1]
                        quantBD += 1
                    except:
                        pass

            except Exception:
                # quando nao conseguir clicar no carro, vai passar a pagina ate nao conseguir, quando nao conseguir,
                # volta pra pagina principal e vai pra outro categoria(linha 123)
                try:
                    car = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, f'//*[@id="listing-cars"]/div[2]/div/div[1]/div[2]/a[{PgPrx}]')))
                    navegador.execute_script('arguments[0].click()', car)
                    pag = pag.replace(f'Pagina={PgAnt}', f'Pagina={PgPrx}')
                    PgAnt = PgPrx
                    PgPrx += 1

                    urlCarro = f'{urlMain}{pag}'
                    print(numPg)

                except Exception:
                    # Quando voltar para a pagina principal, vai quebrar o WHILE e passar a categoria
                    navegador.find_element(
                        By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a').click()
                    numPg += 1
                    cont = len(tabela[' Ano'])

                    x = 1
                    break

            else:
                comando = "INSERT INTO {} (preço, Veículo, Cor, ValorFipe, Ano,Combustível, KM, SituaçãodeEntrada, FinalPlaca, Comitente) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
                    NomeTabela)
                print(listaBD)
                cursor.execute(comando, listaBD)
                conexao.commit()
                navegador.back()
        if not siteCarros:
            navegador.find_element(
                By.XPATH, '//*[@id="sidebar-menu-container"]/div[2]/header/nav/div/a').click()
            break
        if x == 1:
            x = 0
            break
