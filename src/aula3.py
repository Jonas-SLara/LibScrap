import re

def testeRegex(regex, texto):
    x = re.search(regex, texto)
    if x:
        return f"valido: {x.group()}"
    else:
        return None

def testeTelefone():
    print("teste telefone")
    list_regex=[]

    # (ddd) xxx-xxx-xxx
    regex1 = r"\([0-9]{2,3}\) [0-9]{3}-[0-9]{3}-[0-9]{3}"
    list_regex.append(regex1)

    # dd xxxxx xxxx (com () opcionais em volta do DDD)
    regex2 = r"\(?[0-9]{2}\)? [0-9]{5} [0-9]{4}"
    list_regex.append(regex2)

    # dddxxxxxxxxx
    regex3 = r"[0-9]{2,3}[0-9]{8,9}"
    list_regex.append(regex3)

    texto = "número é 55 99999 8888 anote-o"

    for i in list_regex:
        x = testeRegex(i, texto)
        if x:
            print(f"regex: {x}")


#um email tem o formato nome@dominio.extensão
def enderecoWeb(listaEnderecos):
    regex = r"^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}$"
    for i in listaEnderecos:
        if re.fullmatch(regex, i):
            print(f"valido: {i}")
        else:
            print(f"invalido: {i}")


#moedas
# R$3000,00 R$ 3.000,00 3.000,00 reais
def valoresMonetarios(listaMonetarios):
    regex = r"^(R\$ ?[0-9]{1,3}(\.[0-9]{3})*,[0-9]{2})$"
    for valor in listaMonetarios:
        if re.fullmatch(regex, valor):
            print(f"valido: {valor}")
        else:
            print(f"invalido: {valor}")
