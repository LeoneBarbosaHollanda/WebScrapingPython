import site
import pandas as pd
import json
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=BT7_IIuTjYo'


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104"}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
respostas = soup.find(
    "span", class_='style-scope yt-formatted-string bold').get_text()
# print(soup)
# print(site)
print(respostas)
