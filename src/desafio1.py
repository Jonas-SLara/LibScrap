import re

# criar uma regex para validar comentarios em python
def comentariosPython():
    text = "def func (): ### uma função\n" \
    "\"\"\"\n" \
    "Hello World 2\n" \
    "\"\"\"\n"

    regex = r"#.*?\n" #para comentarios em linha
    regex2 = r"['\"]{3}[\s\S]*?['\"]{3}\n" #para comentarios multiplas linhas

    print(text)
    m = re.search(regex, text)
    if m:
        print(m)
    n = re.search(regex2, text)
    if n:
        print(n)
    if (not n or not m):
        print("existem comentarios invalidos")

comentariosPython()

# Criar uma regex para validar endereços de ipv4 192.168.1.1
#4 numeros separados de ponto de 0 a 255
import re

def valida_ip(ip):
    """Verifica se uma string é um endereço IPv4 válido."""
    regex = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    if re.search(regex, ip):
        print(f"'{ip}' é um endereço IP VÁLIDO.")
        return True
    else:
        print(f"'{ip}' é um endereço IP INVÁLIDO.")
        return False

valida_ip("192.168.0.1")
valida_ip("255.255.255.255")
valida_ip("0.0.0.0")
valida_ip("10.0.1.260")
valida_ip("256.1.1.1")
valida_ip("1.2.3.4.5")
valida_ip("123.45.67.890")

# Definir uma regex para estrutura de dicionários em python e sua validação;
import re

def validar_dicionario(dicionario_str):
    """
    Valida a estrutura de um dicionário simples em Python usando regex.
    """
    regex = r""
    
    if re.fullmatch(regex, dicionario_str, re.IGNORECASE):
        print(f"'{dicionario_str}' é uma estrutura de dicionário VÁLIDA.")
        return True
    else:
        print(f"'{dicionario_str}' é uma estrutura de dicionário INVÁLIDA.")
        return False

# Exemplos de uso
validar_dicionario('{"nome": "João", "idade": 30, "ativo": true, "salario": 1500.50}')
validar_dicionario('{"cidade": "Porto Alegre"}')
validar_dicionario('{"item": "relogio", "cor": "prata", "preco": 100}')
validar_dicionario('{"erro": "vírgula no final", "cidade": "Porto Alegre",}')
validar_dicionario('{"nome": "Maria" "idade": 25}')
validar_dicionario('{"dicionario": {"aninhado": 1}}')