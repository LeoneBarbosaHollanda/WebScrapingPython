import requests  as re
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
    with open(filename,'rb')as file:
        binarydata=file.read()
    sqlIncremento='INSERT INTO testefotos (foto) VALUES (%s)'
    mycursor.execute(sqlIncremento,(binarydata, ))
    conexao.commit()

def convertBinaryToFile(binarydata,filename):
    with open(filename,'wb')as file:
        file.write(binarydata) 
url = 'https://www.vipleiloes.com.br/Veiculos/DetalharVeiculo/ca4db281-aeb2-43aa-b933-2b8ace491d65'
site = re.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
fotosLink = soup.find('img',class_='dtp-imgactive')['src']
nome = soup.find('span',class_='dtp-fullnm').get_text().replace('\n',' ').strip().split(' ')
nomeFoto =nome[0].lower()+'.png'
nissan='nissan'
converToBinary("nissan.jpg")

with open(nomeFoto,'wb')as f:
    img=re.get(fotosLink)
    f.write(img.content)
