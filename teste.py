from pathlib import Path
from re import X
import requests
from bs4 import BeautifulSoup
import os
import mysql.connector
pastateste = 'testes'
x='imagem'
localizaçaoteste = Path().absolute()/pastateste
#foto = Path().absolute()/pastateste/'aaaaa.txt'
#localizaçaoteste.mkdir()
"""foto.touch()"""
with pastateste.open('a+')as f:
    with open(x,'wb')as d:    
        img = requests.get('https://armazviplprd.blob.core.windows.net/controle/galeria/padrao/fe5055c3-8fe2-4a3c-9875-a54f34f2c255.jpg')
        d.write(img.content)


print("a localizaçao é esse: ",localizaçaoteste)