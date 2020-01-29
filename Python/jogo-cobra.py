import sys # necessário importar esta biblioteca para readchar() e sys.exit()
import tty # necessário importar esta biblioteca para readchar()
import os # necessário importar esta biblioteca para readchar()
import termios # necessário importar esta biblioteca para readchar()
from random import randint # import para número aleatórios randint(valor min, valor max)

def readchar(): # esta é a implementação do readchar() no Linux, é necessário adicioná-la no programa
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def controlador(a): # função responsável pelo controle do personagem
    a = readchar() # readchar() para input com Enter automático
    if a == 'r':
        clear()
        print('Jogo finalizado com sucesso!\n\n')
        sys.exit()
    return a # retorna a última tecla pressionada

def tabuleiro(tab, p1, p2):
    global x, y, tam, cont, b
    tab[p1][p2] = '\U0001F40D' # posição atual do personagem
    if p1 == x and p2 == y:
        x = randint(0, 9)
        y = randint(0, 9)
        while [x, y] in rastro:
            x = randint(0, 9)
            y = randint(0, 9)
        tab[x][y] = '\U0001F34E' # alimento do personagem em local aleatório
        tam += 1 # tamanho do personagem
    for i, j in rastro: # imprimindo o resto do personagem
        tab[i][j] = '\U0001F40D'
    for a in range(10): # imprimindo o tabuleiro atual
        for b in range(10):
            print(tab[a][b], end = '')
        print()
    print(f"Score \U0001F947 : {tam}\nPosição do personagem \U0001F40D : {p1}, {p2}\nPressione 'r' para sair do jogo \U0001F6AB .")

def colisão(p1, p2, tam): # verifica se houve colisão e fecha o jogo
    if p1 < 0 or p1 > 9 or p2 < 0 or p2 > 9 or [p1, p2] in rastro:
        clear()
        print("Você colidiu!\n")
        sys.exit()
       
# declarações importantes e iniciais
clear = lambda: os.system('clear') # script para clear()
tab = [['\U0001F533' for b in range(10)] for a in range(10)] # criando o tabuleiro usando list comprehesion
p1, p2 = 0, 0 # posição inicial do personagem
x = randint(0, 9) # sorteando o primeiro alimento
y = randint(0, 9)
tab[x][y] = '\U0001F34E' # alimento do personagem
tam = 1 # tamanho inicial da cobra
a = 0 # iniciando o controle
clear()
rastro = [] # lista para guardar o rastro do personagem

def player1(a):
    global p1, p2
    if a == 'w':
        tab[p1][p2] = '\U0001F533' # tornou-se um lugar vazio
        p1 -= 1
    elif a == 's':
        tab[p1][p2] = '\U0001F533' # tornou-se um lugar vazio 
        p1 += 1
    elif a == 'a':
        tab[p1][p2] = '\U0001F533' # tornou-se um lugar vazio
        p2 -= 1
    elif a == 'd':
        tab[p1][p2] = '\U0001F533' # tornou-se um lugar vazio
        p2 += 1

while True: # loop infinito

    tabuleiro(tab, p1, p2)

    if tam > 1:
        rastro.append([p1, p2]) # guardando as novas posições em rastro
    player1(controlador(a))
    colisão(p1, p2, tam)

    g = len(rastro)
    while not g != tam:
        i, j = rastro.pop(0) # retirando as posições antigas da lista
        tab[i][j] = '\U0001F533' # substituindo as posições mais antigas do personagem por uma área vaga
        g += 1
    clear()
    

