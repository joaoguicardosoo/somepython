import urllib.request                           ## módulo para URL
import json                                     ## módulo para JSON

def ManipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    webURL = urllib.request.urlopen(endereco)   ## abre a URL
    if (webURL.getcode() == 200):               ## se tiver sucesso (200 OK)
        dados = webURL.read()                   ## lê a página
        oJSON = json.loads(dados)               ## importa os dados JSON para 'oJSON'

        contagem = oJSON['metadata']['count']   ## contador de quantos metadados
        print('Contagem: ' + str(contagem))     ## printa a contagem

        for local in oJSON['features']:         ## verifica os dados em uma 'tabela'
            if local['properties']['place'] == 'South Sandwich Islands region':
                print('..........Encontrado especial..........')
            print(local['properties']['place'])

ManipulaJSON()                                  ## executa a função
