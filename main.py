"""
1. acessar a página principal
2. encontrar e extrair links das categorias de livros que
estão na página principal
3. depois disso iterar sobre cada link de categoria e para
para cada categoria fazer:
    - acessar a página para cada categoria
"""

from random import random, sample
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import time
import re

listaURLs = ['https://books.toscrape.com/index.html']
listaURLsVisitadas = []
URL_BASE = 'https://books.toscrape.com/'

#função para encontrar os links de 5 categorias
#que preciso, 2 deverão ter paginação que nada mais é
#que um link com botão next na página

def encontrar_links_categorias(bs):
    #div da categ
    categoria = bs.find('div', {'class':{'side_categories'}})
    links = categoria.find_all('a')[1:] #pula o primeiro link que vai para home
    
    listaCategoriasComPaginacao = []
    listaCategoriasSemPaginacao = []
    
    #acessando a url de cada link e vendo se tem paginação
    #tera páginação quando houver um link com a classe next
    for a in links:
        url_rel = a['href']
        url_total = URL_BASE + url_rel
        
        try:
            reqCategoria = Request(
                url=url_total,
                headers={'User-Agent': 'Mozilla/5.0'}  
            )
            htmlCategoria = urlopen(reqCategoria).read()
            time.sleep(2)
            bsCategoria = BeautifulSoup(htmlCategoria, "html.parser")
            
            #verifica se existe o link next na div de paginacao
            pageNext = bsCategoria.find('li', {'class':'next'})
            if pageNext:
                listaCategoriasComPaginacao.append(url_total)
                print(f"url com paginação encontrada - {url_total}")
            else:
                listaCategoriasSemPaginacao.append(url_total)
                print(f"url sem paginação encontrada - {url_total}")
        except URLError as e:
            print(f"erro ao processar a categoria {url_total} {e}")
            continue
    #encontra 3 url nao paginadas e 2 sim
    escolhidas = sample(listaCategoriasComPaginacao, 2) + sample(listaCategoriasSemPaginacao, 3)
   
    return escolhidas

req = Request(
    url=listaURLs[0],
    headers={'User-Agent': 'Mozilla/5.0'}
)

try:
    html = urlopen(req).read()
    time.sleep(2)
    
    bs = BeautifulSoup(html, "html.parser")
    #marca a url como já visitada
    listaURLsVisitadas.append()
    escolhidas = encontrar_links_categorias(bs)
    
    print("***lista de url escolhidas***")
    for u in escolhidas:
        
        print(f"- {u}")
    
except URLError as e:
    print('Servidor não encontrado')
finally:
    print('tudo certo')

