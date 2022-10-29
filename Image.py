import WebScrapingPython
import mysql.connector

# conexao com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='main',

)
nomeTabela = WebScrapingPython.NomeTabela
cursor = conexao.cursor()
comando = "SELECT * FROM {main.tabela35}"
cursor.execute(comando)
imagem = cursor.fetchall()
print(imagem[0][1])
