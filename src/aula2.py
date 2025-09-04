import random
def teoria_tuplas():
    tupla = (1, 2, 3)
    print(tupla)
    #percorrer uma tupla
    for elemento in tupla:
        print(elemento)
    #ou também
    for i in range(len(tupla)):
        temp = type(tupla[i])
        print(f"valor: {tupla[i]} tipo: {temp}")

    #concatenar tuplas a partir de indices delas
    tupla2 = ("a", "b", "c")
    tupla3 = tupla[0:1] + tupla2[0:2] + tupla[1:3] + tupla2[2:3]
    print(tupla3)

    try:
        tupla[0] = 4
    except TypeError:
        print("Erro: Tuplas são imutáveis.")

def listaCompras():
    lista = ["maçã", "banana", "laranja"]
    for item in lista:
        print(item)
    #adicione queijo no final da lista
    lista.append("queijo")
    print(lista)
    #remova a banana da lista
    lista.remove("banana")
    print(lista)
    #remova a laranja da lista pelo indice com pesquisa
    temp = lista.index("laranja")
    lista.pop(temp)
    print(lista)
    #adicione a uva na posição 1
    lista.insert(1, "uva")
    print(lista)
    #imprima o tamanho total da lista
    print(f"Tamanho da lista: {len(lista)}")
    #substitua uva por leite, use index() com parametros para a fatia
    temp = lista.index("uva", 0, len(lista))
    lista[temp] = "leite"
    print(lista)

#Conversão e Junção de Dados:
def conversao_e_juncao():
    t1 = (1,3,5,7,9) #tupla de numeros impares
    t2 = (2,4,6,8,10) #tupla de numeros pares
    # converte as 2 tuplas em listas e juntalas

    lista = list(t1) + list(t2)
    print(lista)

    #agora reordene esta lista
    lista.sort()
    print(lista)

#gere uma lista randômica de tamanho n e retorne
def gerar_lista(n, min, max):
    lista = []
    for _ in range(n):
        lista.append(random.randint(min, max))
    return lista

#dado uma lista de numeros float, implemente uma funçao sort para reordenar em ordem crescente
#sem usar o sort
def ordenar_lista(lista): #este é o método bubble sort
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                temp = lista[j]
                lista[j] = lista[i]
                lista[i] = temp
    return lista

#agora vamos usar o algoritmo quicksort para reordenar
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)

#Cálculo e Contagem de Elementos
def temperaturas_cidade():
    temperaturas = [22.5, 23.9, 18.9, 15.2, 12, 27, 12, 27, 20, 24, 26, 24, 20, 8.7,
                    8.5, 3]
    #media de temperatura
    media = sum(temperaturas) / len(temperaturas)
    print(f"Média de temperatura: {media:.1f}°C")
    #maior temperatura
    maior = max(temperaturas)
    print(f"Maior temperatura: {maior:.1f}°C")
    #menor temperatura
    menor = min(temperaturas)
    print(f"Menor temperatura: {menor:.1f}°C")
    #contagem de temperaturas acima da media
    acima_media = [ x for x in temperaturas if x > media]
    print(f"Temperaturas acima da média:\n {acima_media} \ntotal: {len(acima_media)}")
    #contagem de ocorrencias de 27
    print(f"Temperatura 27°C ocorreu {temperaturas.count(27)} vezes.")

'''
Aninhamento de Estruturas:

Crie uma lista chamada catalogo_produtos. Cada elemento desta lista deve ser 
uma tupla contendo o nome do produto e seu preço. Adicione três produtos de 
sua escolha. Depois:

Imprima o nome e o preço do segundo produto no catálogo;
Adicione um novo produto ("computador", 5000.00) ao catálogo;
Percorra a lista e imprima cada produto no formato: 
"Produto: [nome] - Preço: R$[preço]".
'''

def aninhamento():
    catalogo_produtos = [
        ("celular", 1500.00),
        ("notebook", 3000.00),
        ("tablet", 1200.00)
    ]
    
    # Imprime o nome e o preco do segundo produto
    print(f"{catalogo_produtos[1][0]} valor: {catalogo_produtos[1][1]:.2f}")
    # Adiciona um novo produto ao catálogo
    catalogo_produtos.append(("computador", 5000.00))

    #percorre a lista
    for produto in catalogo_produtos:
        print(f"Produto: {produto[0]} - Preço: R${produto[1]:.2f}")

#Dicionários

def teoria_dos_dicionarios():
    dicionario = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo"
    }
    print(dicionario)
    # Acessando valores
    print(dicionario["nome"])
    # Adicionando novos pares chave-valor
    dicionario["profissao"] = "Engenheiro"
    print(dicionario)
    # Removendo um item
    del(dicionario["idade"])
    # Alterando um item
    dicionario["cidade"] = "Rio de Janeiro"
    dicionario["nome"] = "Felipe"
    print(dicionario)

    #percorrendo um dicionario
    print(dicionario.items())
    for i in dicionario.items():
        print(f"chave: {i[0]} \t valor: {i[1]}")


def aluno():
    aluno = {}
    aluno["nome"] = str(input("Digite o nome do aluno: "))
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["curso"] = str(input("Digite o curso do aluno: "))
    aluno["telefone"] = str(input("Digite o telefone do aluno: "))

    endereco = {}
    endereco["rua"] = str(input("Digite o nome da rua: "))
    endereco["numero"] = int(input("Digite o número da casa: "))
    endereco["cidade"] = str(input("Digite o nome da cidade: "))
    aluno["endereco"] = endereco

    #printa o aluno
    for chave, valor in aluno.items():
        if chave == "endereco":
            for chave_endereco, valor_endereco in valor.items():
                print(f"{chave_endereco} : {valor_endereco}")
        else:
            print(f"{chave} : {valor}")
    return aluno

def agenda_telefonica(n):
    lista = []
    for i in range(n):
        agenda = {}
        agenda["nome"] = str(input("Digite o nome do contato: "))
        agenda["contato"] = str(input("Digite o telefone do contato: "))
        lista.append(agenda)
    #printa a lista
    print("Agenda Telefônica:")
    for contato in lista:
        for chave, valor in contato.items():
            print(f"{chave} : {valor}")
    return lista

#calcular a taxa de similiaridade de 2 conjuntos
#dado 2 dicionários, pegue a quantidade de valores chaves em comum
#taxa = total de ocorrencias / qtd total de valores distinto
def similiaridade(dicionario1, dicionario2):
    total_ocorrencias = 0
    for chave in dicionario1.keys():
        for chave2 in dicionario2.keys():
            if chave == chave2:
                print(f"Chave em comum: {chave}")
                total_ocorrencias+=1
    print(f"total ocorrencias: {total_ocorrencias}")

    elementos_distintos = len(dicionario1) + len(dicionario2) - total_ocorrencias
    print(f"Elementos distintos: {elementos_distintos}")

    taxa_similaridade = total_ocorrencias / elementos_distintos
    print(f"Taxa de similaridade: {taxa_similaridade:.2f}")

def teste_dicionarios():
    dicionario1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    dicionario2= {"a": 1, "b": 2, "c":3, "f": 6}
    similiaridade(dicionario1, dicionario2)
    print()
    dicionario1.pop("e")
    similiaridade(dicionario1, dicionario2)