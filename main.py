# resoluçoes de exercicios em python estão nos imports aqui será testado
from datetime import datetime
import src.aula1 as aula1
import src.aula2 as aula2
import src.aula3 as aula3
import time

def testeOrdenacao():
    temp = aula2.gerar_lista(100000, 1, 100000)  
    t = time.time()
    aula2.quicksort(temp)
    print("tempo de execução quicksort: %f" %(time.time() - t))

lista = [
    "joao.silva@gmail.com",    # válido
    "ana_123@ufsm.br",         # válido
    "teste-user@empresa.co.uk",# válido
    "maria@site",              # inválido (sem TLD)
    "fulano@.com",             # inválido (domínio começa com .)
    ".joao@site.com",          # inválido (nome começa com ponto)
]

#aula3.enderecoWeb(lista)

listaMonetarios=[
    "R$ 3.000,00",
    "R$399,00",
    "R$2",
    "R$2,00",
    "R$ 2222,00",
    "R$ 2.222,00",
    "R$ 2.000.000,27"
]

aula3.valoresMonetarios(listaMonetarios)


