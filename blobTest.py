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
    sqlIncremento='INSERT INTO testefotos (foto1,foto2,foto3,foto4) VALUES (%s,%s,%s,%s)'
    mycursor.execute(sqlIncremento,(binarydata, ))
    conexao.commit()

def convertBinaryToFile(binarydata,filename):
    with open(filename,'wb')as file:
        file.write(binarydata) 
url = 'https://www.vipleiloes.com.br/Veiculos/DetalharVeiculo/ca4db281-aeb2-43aa-b933-2b8ace491d65'
site = re.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
fotosLink = soup.find_all('img',class_='dtp-imgactive')
nome = soup.find('span',class_='dtp-fullnm').get_text().replace('\n',' ').strip().split(' ')



for a,c in enumerate(fotosLink):
    print(c['src'])
    nomeFoto =nome[0].lower()+f'{a}.jpg'
    with open(nomeFoto,'wb')as f:
        img=re.get(c['src'])
        f.write(img.content)
