
1. Planejamento e Análise do Alvo:

1. Como a navegação entre as categorias funciona (links na barra lateral)?
    - a navegacao entre as categorias ocorrem entre links na barra lateral
    que são padronizadas em cada página com a seguinte estrutura:

> https://books.toscrape.com/index.html
> https://books.toscrape.com/catalogue/category/books_1/index.html
> https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html

    <ul class="nav nav-list">         
        <li>
            <a href="../../books_1/index.html">Books</a>
        </li>
        <ul>
            <li><a href="../travel_2/index.html">Travel</a></li>
        </ul>
        ...outros irmões...
    <ul>
        

2. Como a paginação funciona dentro de uma categoria ou na página principal (botão "next")?
    - tanto na página principal como na página das categorias que tem paginação
    há a seguinte estrutura: 

    <ul class="pager">
        <li class="current">Page 1 of 3</li>
        <li class="next"><a href="page-2.html">next</a></li>
    </ul>    
        

3. Qual a estrutura da página de um livro individual? (Onde estão o título, preço, avaliação, etc.?)
    - os livros estão em uma lista ordenada onde cada um é um item desta lista
    dentro dele há uma seção article com a classe 'product_pod' e as informações estão dispostas
    na seguinte estrutura

    <li>
        <article class="product_pod">
            ...outros elementos irmãos...
            <h3><a href="../../../the-mistake-off-campus-2_851/index.html" title="The Mistake (Off-Campus #2)">The Mistake (Off-Campus #2)</a></h3>
            ...outros elementos irmãos...
        </article>
    </li>

    Ao acessar a página específica do livro temos uma estrutura parecida com essa

    >> https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html

    <ul class="breadcrumb">
        <li>
            <a href="../../index.html">Home</a>
        </li>
        <li>
            <a href="../category/books_1/index.html">Books</a>
        </li>
        <li>
            <a href="../category/books/fantasy_19/index.html">Fantasy</a>
        </li>
        
        <li class="active">Unicorn Tracks</li>
    </ul>

    conteudo do livro dentro de uma div com a classe 'content'
    
4. Crawling por Categorias e Paginação:

Tarefa: O script deve ser capaz de encontrar todos os livros das categorias escolhidas de forma automatizada;

Passo 1 - Crawling de Categorias: O script deve primeiro acessar a página inicial, encontrar e extrair os links das categorias de livros escolhidas que estão listadas na barra lateral;

Passo 2 - Crawling de Livros: O script deve então iterar sobre cada link de categoria. Para cada categoria:

    Acessar a página da categoria;
    Coletar os links de todos os livros da página atual;
    Enquanto houver um botão "next" (próxima página), o crawler deve segui-lo, repetindo o processo de coleta de links.
    Resultado Final da Etapa: Uma lista contendo as URLs de todos os livros.
    
3. Scraping e Extração com Regex:

Tarefa: Com a lista de URLs de todos os livros, o script deve visitar cada uma e extrair as seguintes informações:

Título do Livro: (Extração direta com BeautifulSoup);

Preço: (Extração direta do texto, ex: £51.77);

Categoria: (Extração do "breadcrumb" de navegação no topo da página);

Avaliação: A avaliação está na classe da tag p (ex: star-rating Three). O aluno deve extrair a palavra correspondente à avaliação (ex: "Three", "One", "Five");

Disponibilidade: O texto que informa a quantidade em estoque (ex: "In stock (22 available)");

UPC (Código Universal do Produto): Disponível na tabela de informações do produto.

Uso Obrigatório de Expressões Regulares (Regex):

Do texto da Disponibilidade, o aluno deve usar Regex para extrair apenas o número de livros em estoque. Por exemplo, de "In stock (22 available)", extrair o inteiro 22;

Do texto do Preço, o aluno deve usar Regex para extrair apenas o valor numérico, removendo o símbolo da moeda (£). Por exemplo, de "£51.77", extrair o float 51.77. Ainda com regex, substituir o separador decimal ponto (.) por vírgula (,).

4. Gerar um arquivo externo (ex: .csv) com compilação das informações extraídas (pesquisar sobre).
