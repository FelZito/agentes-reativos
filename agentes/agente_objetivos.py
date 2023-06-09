import os

class AgenteObjetivos:
    def __init__(self, matriz):
        self.matriz = matriz
        self.posX, self.posY = self.loc_robo() # posX - linha | posY - coluna
        
    def loc_robo(self):
        # Verifica posição inicial do robô
        for linha in range(len(self.matriz)):
            for coluna in range(len(self.matriz[linha])):
                if self.matriz[linha][coluna] == '\U0001F916':
                    return linha, coluna

    def move_direita(self, linha, coluna):
        while self.posY < coluna:
            self.matriz[self.posX][self.posY] = '-'
            self.posY += 1
            self.matriz[self.posX][self.posY] = '\U0001F916'
            #self.print_matriz(1)
        return self.posX, self.posY

    def mov_esquerda(self, linha, coluna):
        while self.posY > coluna:
            self.matriz[self.posX][self.posY] = '-'
            self.posY -= 1
            self.matriz[self.posX][self.posY] = '\U0001F916'
            #self.print_matriz(1)
        return self.posX, self.posY

    def mov_baixo(self, linha, coluna):
        while self.posX < linha:
            self.matriz[self.posX][self.posY] = '-'
            self.posX += 1
            self.matriz[self.posX][self.posY] = '\U0001F916'
            #self.print_matriz(1)
        return self.posX, self.posY

    def mov_cima(self, linha, coluna):
        while self.posX > linha:
            self.matriz[self.posX][self.posY] = '-'
            self.posX -= 1
            self.matriz[self.posX][self.posY] = '\U0001F916'
            #self.print_matriz(1)
        return self.posX, self.posY

    def executar(self):
        # encontrar posições alvo e mover o robô para cada uma
        lixos = ['r', 'o']
        for lixo in lixos:
            for linha in range(len(self.matriz)):
                for coluna in range(len(self.matriz[linha])):
                    if self.matriz[linha][coluna] == lixo:
                        # mover o robô para a posição do lixo
                        linha = linha
                        coluna = coluna
                        if self.posY < coluna:
                            self.posX, self.posY = self.move_direita(linha, coluna)
                            self.print_matriz(1)
                        if self.posY > coluna:
                            self.posX, self.posY = self.mov_esquerda(linha, coluna)
                            self.print_matriz(1)
                        if self.posX < linha:
                            self.posX, self.posY = self.mov_baixo(linha, coluna)
                            self.print_matriz(1)
                        if self.posX > linha:
                            self.posX, self.posY = self.mov_cima(linha, coluna)
                            self.print_matriz(1)

    def print_matriz(self, status):
        if status == 1:
            for linha in self.matriz:
                print(' '.join(linha))
            print('\n')
            #input()
            os.system('clear' if os.name == 'posix' else 'cls')  # limpa a tela do terminal
        else:
            for linha in self.matriz:
                print(' '.join(linha)) # Imprime sem limpar a tela
            print('\n')