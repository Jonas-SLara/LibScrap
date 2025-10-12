from bs4 import BeautifulSoup
import time
import re
from urllib.request import Request, urlopen
from urllib.error import URLError

#é tipo um enum em java só que aqui é para a classe de avaliação
MAPA_AVALIACAO = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

def obter_livros(linkLivros):

    livros = []

    for l in linkLivros:
        try:
            requisicao = Request(
                url = l,
                headers = {'User-Agent': 'Mozilla/5.0'}
            )
            html = urlopen(requisicao).read()
            time.sleep(1)
            bsLivro = BeautifulSoup(html, "html.parser")
            livroPage = bsLivro.find('article', class_="product_page")
            breadcrump = bsLivro.find('ul', class_='breadcrumb')

            rgexValor = re.compile(r"\d+\.\d\d")
            rgexDispo = re.compile(r"\d+")

            livro = obter_dados_livro(livroPage, breadcrump, rgexValor, rgexDispo)
            
            livros.append(livro)
            livro_texto_dados(livro)

        except URLError as e:
            print(f"erro ao processar livro {e}")
            continue

    return livros
    
#objeto da estrutura html do livro dado pela função find para extração
def obter_dados_livro(livro, breadcrump, rgexValor, rgexDispo):
    dLivro = {}
    #pegar o título
    titulo = livro.find('h1').text
    dLivro["titulo"] = titulo

    #pegar o valor apenas
    preco = livro.find('p', class_="price_color").text
    m = re.search(rgexValor, preco)
    #substitui . por ,
    dLivro["preco"] = re.sub( r"\.", ',', m.group())

    #estoque disponivel
    estoque = livro.find('p', {'class' : {'instock', 'availability'}}).text
    m = re.search(rgexDispo, estoque)
    dLivro["disponivel"] = m.group()
    
    #avaliacao
    avaliacao = livro.find('p', {'class': 'star-rating'})
    if avaliacao:
        classes = avaliacao['class']
        nomeAvaliacao = classes[1] if len(classes) > 1 else None
        nota = MAPA_AVALIACAO.get(nomeAvaliacao, 0) #0 se não tiver
        dLivro["nota"]=nota
    else:
        dLivro["nota"]=0 #0 se não tiver nada
    
    #UPC começa em none e se achar muda
    upc = None
    tabelaInfo = livro.find('table', {'class': {'table', 'table-striped'}})
    if tabelaInfo:
        cabecalho = tabelaInfo.find('th', string="UPC")
        if cabecalho:
            upc = cabecalho.find_next_sibling('td').text.strip()
    dLivro["upc"] = upc
    
    #Extrair categoria de breadcrump,
    categoria = None
    if breadcrump:
        links = breadcrump.find_all('a')
        if len(links) >= 3:
            categoria = links[2].text.strip()
    dLivro["categoria"] = categoria

    return dLivro

def livro_texto_dados(livro):
    for chave, valor in livro.items():
        print(f"{chave} : {valor}")
    print('\n')


