import os

class AgenteSimples:
    def __init__(self, matriz):
        self.matriz = matriz
        self.robo = '\U0001F916'
        self.lixeira = '\U0001F5D1'

    def print_matriz(self, status):
        if status == 1:
            for linha in self.matriz:
                for elemento in linha:
                    print(elemento, end=" ")
                print()
            #input()
            os.system('clear')
        else:
            for linha in self.matriz:
                for elemento in linha:
                    print(elemento, end=" ")
                print()
    
    def coletar_lixo(self, linha, coluna):
        self.matriz[linha][coluna] = "-"
        self.matriz[linha][coluna+1] = self.robo

    def no_op(self, linha, coluna):
        self.matriz[linha][coluna] = "-"
        self.matriz[linha][coluna+1] = self.robo

    def executar(self):
        for linha in range(20):
            for coluna in range(20):
                # Verifica se existe coluna ao lado, caso não tenha desce para a linha de baixo
                if coluna < len(self.matriz[linha]) - 1: 
                    if self.matriz[linha][coluna+1] == "-":
                        self.no_op(linha, coluna)
                        self.print_matriz(1)
                    elif self.matriz[linha][coluna+1] == "r" or self.matriz[linha][coluna+1] == "o":
                        self.coletar_lixo(linha, coluna)
                        self.print_matriz(1)
                    else:
                        return False
                else:
                    # Move o robô para a linha de baixo
                    self.matriz[linha+1][0] = self.robo
                    self.matriz[linha][coluna] = "-"
                    self.print_matriz(1)