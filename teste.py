import random
from agente_simples import *

# Cria aleatoriamente uma matriz e a preenche com "-"
matriz = [["-" for j in range(20)] for i in range(20)]

# Adiciona aleatoriamente os lixos "a" e "v" na matriz
for i in range(15):
    x, y = random.randint(0, 19), random.randint(0, 19)
    valor = random.choice(["r", "o"])
    matriz[x][y] = valor

# Define a posição do robô e da lixeira
matriz[0][0] = '\U0001F916'
matriz[19][19] = "\U0001F5D1"

while True:
    print("|| MENU PRINCIPAL ||")
    print("""
    1 - Agente reativo simples

    0 - Sair
    """)

    op = int(input("Informe a opção desejada: "))

    if op == 1:
        agente_simples = AgenteSimples(matriz)
        agente_simples.executar()

    elif op == 0:
        print("Saindo do programa...")
        exit(1)