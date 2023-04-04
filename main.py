import random, time
from agentes.agente_objetivos import *
from agentes.agente_simples import *

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

# Guarda os valores da matriz original em uma nova matriz
reset_matriz = [[valor for valor in linha] for linha in matriz]

while True:
    print("""
    || MENU PRINCIPAL ||
    1 - Agente reativo simples
    2 - Agente reativo baseado em objetivos
    0 - Sair
    """)

    op = int(input("Informe a opção desejada: "))

    if op == 1:
        robo_simples = AgenteSimples(matriz)
        print("="*40)
        print("           MATRIZ ORIGINAL         ")
        print("="*40)
        robo_simples.print_matriz(0)

        input("Aperte enter para iniciar")

        inicio = time.perf_counter()
        robo_simples.executar( )
        fim = time.perf_counter()

        matriz[:] = [linha[:] for linha in reset_matriz]

        tempo_execucao = (fim - inicio) * 1000

        print(f"O tempo de execução foi: {tempo_execucao:.2f} ms")

        # Reseta matriz para o agente iterar sobre a matriz original
        matriz[:] = [linha[:] for linha in reset_matriz]

    elif op == 2:
        robo = AgenteObjetivos(matriz)
        print("="*40)
        print("           MATRIZ ORIGINAL         ")
        print("="*40)
        robo.print_matriz(0)

        input("Aperte enter para iniciar")

        inicio = time.perf_counter()
        robo.executar( )
        fim = time.perf_counter()

        tempo_execucao = (fim - inicio) * 1000
    
        print(f"O tempo de execução do agente reativo simples foi: {tempo_execucao:.2f} ms")

        # Reseta matriz para o agente iterar sobre a matriz original
        matriz[:] = [linha[:] for linha in reset_matriz]

    elif op == 0:
        print("Saindo do programa...")
        exit(1)

    else:
        print("Informe uma opção válida...")