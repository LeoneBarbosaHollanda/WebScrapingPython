
dicUrl = {'porshe': '9a0bebee-1255-4dff-8474-c913eae51c38',
          'suzuki': 'd9aac9e4-23d8-4fc6-884b-34570151dcc0',
          'chevrolet': '8c951ce0-f26b-4b87-887a-1b46ba967748',
          'ford': 'e09be6d3-f527-4e38-9243-562b84c859a2'}


def urlCarros(url):
    url = f'https://www.vipleiloes.com.br/Veiculos/DetalharVeiculo/{dicUrl[url]}'
    return url
