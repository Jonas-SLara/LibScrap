from bs4 import BeautifulSoup
from random import shuffle
import time
import re
from urllib.request import Request, urlopen
from urllib.error import URLError

#função para encontrar os links absolutos na seção de links
#da página principal de todas as categorias

def encontrar_links_categorias(URL_BASE):

    req = Request(
        url=URL_BASE + "index.html",
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    html = urlopen(req).read()
    time.sleep(2)
    bs = BeautifulSoup(html, "html.parser")

    categoria = bs.find('div', {'class':{'side_categories'}})
    links = categoria.find_all('a')[1:] #pula o primeiro link que vai para home
    
    listaLinksCategorias = []
    for a in links:
        # exemplo de retorno = catalogue/category/books/travel_2/index.html
        url_rel = a['href']
        #adiciona a url total na lista de links para as cetegorias
        listaLinksCategorias.append(URL_BASE + url_rel)
    shuffle(listaLinksCategorias)
    return listaLinksCategorias

# função que apartir de uma lista de links escolhe 3 sem paginação e 2 com aleatoriamente
# e ao final para quando achar
def escolher_links_categorias(lista):
    listaCategoriasComPaginacao = []
    listaCategoriasSemPaginacao = []

    for l in lista:   
        if len(listaCategoriasComPaginacao) >= 2 and len(listaCategoriasSemPaginacao) >= 3:
            break 
        try:
            reqCategoria = Request(
                url=l,
                headers={'User-Agent': 'Mozilla/5.0'}  
            )
            htmlCategoria = urlopen(reqCategoria).read()
            time.sleep(1)
            bsCategoria = BeautifulSoup(htmlCategoria, "html.parser")
            
            #verifica se existe o link next na div de paginacao
            pageNext = bsCategoria.find('li', {'class':'next'})
            
            if pageNext and len(listaCategoriasComPaginacao) < 2:
                listaCategoriasComPaginacao.append(l)
                print(f"url com paginação encontrada - {l}")
            elif len(listaCategoriasSemPaginacao) < 3:
                listaCategoriasSemPaginacao.append(l)
                print(f"url sem paginação encontrada - {l}")
        except URLError as e:
            print(f"erro ao processar a categoria {l} {e}")
            continue

    escolhidas = listaCategoriasComPaginacao + listaCategoriasSemPaginacao
   
    return escolhidas

#Função para buscar os links absolutos de todos os livros
#em cada categoria, exemplo de um caminho para um livro
def encontrar_links_livros(URL_ABSOLUTO, categorias, indice=0):
    if indice < len(categorias)-1:
        print(f"*** {indice + 1} de {len(categorias)} ***")
        lista_links_livros = navegar_paginas_livros(URL_ABSOLUTO, categorias[indice])
        return lista_links_livros + encontrar_links_livros(URL_ABSOLUTO, categorias, indice+1)
    else:
        return []

#../../../judo-seven-steps-to-black-belt-an-introductory-guide-for-beginners_903/index.html
# para ->
#https://books.toscrape.com/catalogue/aladdin-and-his-wonderful-lamp_973/index.html 

def arumar_links_livros(links_livros, URL_BASE):
    regex = re.compile(r"^(\.\./){3}")

    for i in range(0, len(links_livros)):
        links_livros[i] = URL_BASE + re.sub(regex, 'catalogue/', links_livros[i])
        
def navegar_paginas_livros(URL_BASE, categoriaLink):
    try:
        reqCategoria = Request(
            url=categoriaLink,
            headers={'User-Agent': 'Mozilla/5.0'}  
        ) 

        htmlCategoria = urlopen(reqCategoria).read()
        time.sleep(2)
        bsCategoria = BeautifulSoup(htmlCategoria, "html.parser")

        print(f"URL ATUAL -> {categoriaLink}")    
        livros = bsCategoria.find_all('article', class_="product_pod")
        lista_links_absolutos = []
        for l in livros:
            a = l.find('h3').find('a')
            link_relativo = a['href']
            lista_links_absolutos.append(link_relativo)

        # ve se tem paginação e
        #troca o link da página da categoria atual pela sua próxima trocando o html
        next_li = bsCategoria.find('li', class_="next")
        if next_li:
            proxima = next_li.find('a')['href']
            proximaPagina = re.sub(r"[^/]+\.html$", proxima, categoriaLink)
            lista_links_absolutos += navegar_paginas_livros(URL_BASE, proximaPagina)

        return lista_links_absolutos
        
    except URLError as e:
        print(f"erro ao acessar URL da categoria: {e}")  
        return []
        
