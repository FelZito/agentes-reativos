import random, time
from Robo import *

# Cria aleatoriamente uma matriz e a preenche com "-"
matriz = [["-" for j in range(20)] for i in range(20)]

# Adiciona aleatoriamente os lixos "a" e "v" na matriz
for i in range(15):
    x, y = random.randint(0, 19), random.randint(0, 19)
    valor = random.choice(["r", "o"])
    matriz[x][y] = valor

# Define a posição do robô e da lixeira
matriz[0][0] = "<@>"
matriz[19][19] = "\\_/"

robo = Robo(matriz)

print("""
==================================
         MATRIZ ORIGINAL
==================================
""")
robo.print_matriz(0)

input("Aperte enter para iniciar")

inicio = time.perf_counter()
robo.executar( )
fim = time.perf_counter()

tempo_execucao = (fim - inicio) * 1000

print(f"O tempo de execução foi: {tempo_execucao:.2f} ms")