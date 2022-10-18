import requests as re
from bs4 import BeautifulSoup
import os
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='main'

)
mycursor = conexao.cursor()


def converToBinary(filename):
    with open(filename, 'rb')as file:
        binarydata = file.read()
    sqlIncremento = 'INSERT INTO testefotos (fotos) VALUES (%s)'
    mycursor.execute(sqlIncremento, (binarydata, ))
    conexao.commit()


def convertBinaryToFile(binarydata, filename):
    with open(filename, 'wb')as file:
        file.write(binarydata)


url = 'https://www.vipleiloes.com.br/Veiculos/DetalharVeiculo/aac62c80-36f7-44fa-aaf6-9e71dfd9778d'
site = re.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
fotosLink = soup.find_all('img', class_='dtp-imgactive')
for i, fotos in enumerate(fotosLink):
    fotos[i] = fotos['src']
print(fotos)
"""nome = soup.find(
    'span', class_='dtp-fullnm').get_text().replace('\n', ' ').strip().split(' ')
nomeFoto = nome[0].lower()+'.png'"""
"""
print(fotosLink)
with open(nomeFoto, 'wb')as f:
    img = re.get(fotosLink)
    f.write(img.content)
converToBinary(nomeFoto)"""
