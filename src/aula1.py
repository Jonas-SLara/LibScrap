from datetime import datetime, timedelta

# Função para exibir mensagem de boas-vindas
def mensagem_boasVindas():
    print("Olá Mundo %d" % 42)
    print("Seja bem-vindo à aula de Python!")
    return

#retorna a média aritmética de 2 números
def media_aritmetica(x, y):
    return (x + y) / 2

#algoritmo que le um valor, selecione a forma de pagamento e calcule o valor total
#a vista em dinheiro = 10% desconto a vista no crédito = 15% desconto em 2 vezes 10% juros 
#tem que ter tratamento de erros para validar a entrada do usuario
def forma_de_pagamento():
    try:
        print("valor do produto")
        valor = float(input("Digite o valor do produto: "))
        print("Selecione a forma de pagamento:")
        print("1 - a vista em dinheiro\n" \
        "2 - a vista no crédito\n" \
        "3 - em 2 vezes\n")
        op = int(input("selecione a forma de pagamento: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None
    if op == 1:
        print("Você selecionou a vista em dinheiro")
        valor = valor * 0.9
    elif op == 2:
        print("Você selecionou a vista no crédito")
        valor = valor * 0.85
    elif op == 3:
        print("Você selecionou em 2 vezes")
        valor = valor * 1.1
    else:
        print("Opção inválida")
    return valor

#Faça um programa para ler diversos valores para duas variáveis inteiras
# até que a primeira seja menor que a segunda. 
def leituraMenor():
    try:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        while(True):
            if x < y:
                break
            x = int(input("Digite o primeiro valor: "))
            y = int(input("digite o segundo valor: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return False
    return True

#Desenvolva um algoritmo que somente permita a leitura de valores maiores que os lidos 
# anteriormente. Você deve definir uma condição de parada para o programa. 
# mesmo esquema, se for menor que o segundo para
def leituraMaior():
    try:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        while(True):
            if x > y:
                break
            while(True):
                temp = int(input("Digite o primeiro valor: "))
                if temp < x:
                    print("O valor deve ser maior que %d" % x)
                else:
                    x = temp
                    break
            while(True):
                temp = int(input("digite o segundo valor: "))
                if temp < y:
                    print("O valor deve ser maior que %d" % y)
                else:
                    y = temp
                    break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return False
    return True

#Faça uma função que verifique se um valor é perfeito ou não
def perfeito(n):
    soma = 0
    #o maior divisor de um numero é n//2, só por garantia + 1, isso melhora o algoritmo
    for i in range(1, n//2 + 1, 1):
        if n % i == 0:
            print(i)
            soma += i
            print(soma)
    if soma == n:
        print("%d é um número perfeito" % n)
        return True
    else:
        print("%d não é um número perfeito" % n)
        return False

#Desenvolva um algoritmo com uma função que recebe por parâmetro a hora de início e término de um jogo, 
#ambas subdivididas em 2 valores distintos: horas e minutos. A função deve apresentar a duração do jogo 
#em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo
#pode começar em um dia e terminar no outro. 
def duracao_jogo(h_inicio, m_inicio, h_fim, m_fim):
    if h_fim < h_inicio or (h_fim == h_inicio and m_fim < m_inicio):
        h_fim += 24  # Ajusta para o dia seguinte
    duracao_jogo = (h_fim*60 + m_fim) - (h_inicio*60 + m_inicio)
    duracao_horas = duracao_jogo // 60
    duracao_minutos = duracao_jogo % 60
    print("Duração do jogo: %d horas e %d minutos" % (duracao_horas, duracao_minutos))
    return

def duracao_jogo2(data_inicio, data_fim):
    duracao = data_fim - data_inicio
    print("Duração do jogo: %d horas e %d minutos" % (duracao.seconds // 3600, (duracao.seconds // 60) % 60))
    return


