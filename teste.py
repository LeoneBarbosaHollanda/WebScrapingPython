import os
from pathlib import Path
from glob import glob
import requests
from bs4 import BeautifulSoup
import os
import mysql.connector
pastateste = 'testes'
x = 'imagem.txt'
localizaçaoteste = Path().absolute()
localizaçaoteste = localizaçaoteste / 'testes'
print(localizaçaoteste)
#foto = Path().absolute()/pastateste/'aaaaa.txt'
# localizaçaoteste.mkdir()
"""foto.touch()"""

os.chdir(localizaçaoteste)
with open('image.txt', 'wb') as f:
    """img = requests.get('aaaa.txt')
    f.write(img.content)"""


#print("a localizaçao é esse: ", localizaçaoteste)
