
from urllib.error import HTTPError, URLError
from src import WebScrap as ws
from src import webCrawling as wc
from src import MakeCSV as mc

URL_BASE = 'https://books.toscrape.com/'

try:
    
    encontradas = wc.encontrar_links_categorias(URL_BASE)
    
    escolhidas = wc.escolher_links_categorias(encontradas)

    print("***URL escolhidas***")
    for x in escolhidas:
        print(x)

    linkLivros = wc.encontrar_links_livros(URL_BASE, escolhidas, 0)

    wc.arumar_links_livros(linkLivros, URL_BASE)

    #lista de dicionarios
    livros = ws.obter_livros(linkLivros)

    #tranfosrma os dados de livros em csv
    mc.salvar_livros_csv(livros, "livros.csv")

except URLError as e:
    print('Servidor não encontrado')
except HTTPError as e:
    print(f'falha na requisição {e}')
finally:
    print('tudo certo')



