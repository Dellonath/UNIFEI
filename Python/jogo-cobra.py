import sys # necessário importar esta biblioteca para readchar() e sys.exit()
import tty # necessário importar esta biblioteca para readchar()
import os # necessário importar esta biblioteca para readchar()
import termios # necessário importar esta biblioteca para readchar()
from random import randint # import para número aleatórios randint(valor min, valor max)
from random import choice # randomizar elementos de lista choice(lista)
import time

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
    a = readchar().lower() # readchar() para input com Enter automático
    if a == 'r':
        clear()
        print('Jogo finalizado com sucesso!\n\n')
        sys.exit()
    return a # retorna a última tecla pressionada

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tabuleiro(tab, p1, p2, p3, p4, p5, p6):
    global x, y, tam, cont, b, tambot, tambot1, bots
    if p1 == x and p2 == y:
        x = randint(0, 19)
        y = randint(0, 19)
        while [x, y] in rastro or [x, y] in rastrobot or [x, y] in rastrobot1:
            x = randint(0, 19)
            y = randint(0, 19)
        tab[x][y] = choice(alimentos) # alimento do personagem em local aleatório
        t = True
        if bots == 0:
            if t:
                tab[p3][p4], tab[p5][p6] = '\U00002B1B', '\U00002B1B'
                tambot -= 1
                tambot1 -= 1
                t = False
            tam += 1 # tamanho do personagem
        elif bots == 1:
            tam += 1 # tamanho do personagem
            tambot += 1 # tamanho do personagem bot
            tab[p5][p6] = '\U00002B1B'
        elif bots == 2:
            tam += 1 # tamanho do personagem
            tambot += 1 # tamanho do personagem bot
            tambot1 += 1 # tamanho do personagem bot 1
    elif p3 == x and p4 == y:
        x = randint(0, 19)
        y = randint(0, 19)
        while [x, y] in rastro or [x, y] in rastrobot or [x, y] in rastrobot1:
            x = randint(0, 19)
            y = randint(0, 19)
        tab[x][y] = choice(alimentos) # alimento do personagem em local aleatório
    elif p5 == x and p6 == y:
        x = randint(0, 19)
        y = randint(0, 19)
        while [x, y] in rastro or [x, y] in rastrobot or [x, y] in rastrobot1:
            x = randint(0, 19)
            y = randint(0, 19)
        tab[x][y] = choice(alimentos) # alimento do personagem em local aleatório

    for i, j in rastro:  # imprimindo o resto do personagem
        tab[i][j] = '\U0001F539'
    for i, j in rastrobot:  # imprimindo o resto do personagem bot
        tab[i][j] = '\U0001F538'
    for i, j in rastrobot1:  # imprimindo o resto do personagem bot
        tab[i][j] = '\U0001F538'
    for a in range(20): # imprimindo o tabuleiro atual
        for b in range(20):
            print(tab[a][b], end = '')
        print()
    print(f"Score \U0001F947 : {tam}\nPosição do personagem \U0001F40D : {p1 + 1}, {p2 + 1}\nPressione 'r' para sair do jogo \U0001F6AB.")

def colisão(p1, p2, p3, p4, tam): # verifica se houve colisão e fecha o jogo
    if [p1, p2] in rastro:
        clear()
        print("Você colidiu contra si mesmo! Aguarde.\n")
        time.sleep(3)
        restart_program()
    elif [p1, p2] in rastrobot or [p1, p2] in rastrobot1:
        clear()
        print("Você colidiu contra a cobra bot! Aguarde.\n")
        time.sleep(3)
        restart_program()
    elif [p3, p4] in rastro or [p5, p6] in rastro:
        clear()
        print("Você foi atingido pela cobra bot! Aguarde.\n")
        time.sleep(3)
        restart_program()

def player1(a):
    global p1, p2, p3, p4
    if tam > 1:
        rastro.append([p1, p2]) # guardando as novas posições em 
    tab[p1][p2] = '\U00002B1B' # tornou-se um lugar vazio
    if a == 'w':      
        p1 -= 1
    elif a == 's':
        p1 += 1
    elif a == 'a':
        p2 -= 1
    elif a == 'd':
        p2 += 1
    p1, p2 = correção(p1, p2)
    colisão(p1, p2, p3, p4, tam)
    colisão(p1, p2, p5, p6, tam)
    g = len(rastro)
    while not g != tam:
        i, j = rastro.pop(0) # retirando as posições antigas da lista
        tab[i][j] = '\U00002B1B' # substituindo as posições mais antigas do personagem por uma área vaga
        g += 1
def correção(p3, p4):
    if p3 > 19: # o bot não sofre com colisões no fim do tabuleiro
        p3 = 0
    if p3 < 0:
        p3 = 19
    if p4 > 19:
        p4 = 0
    if p4 < 0:
        p4 = 19
    return p3, p4

def bot(p3, p4, tambot, rastrobot):
    global tam
    if tambot > 1:
        rastrobot.append([p3, p4]) # guardando as novas posições em rastro
    tab[p3][p4] = '\U00002B1B'
    a = p3
    b = p4
    while True:    
        mov = randint(0, 3)     
        if mov == 0: # movimentação contínua do bot
            p3 += 1
            p3, p4 = correção(p3, p4)
            if not tab[p3][p4] == '\U0001F538':
                break
            p3 -= 1
        elif mov == 1:
            p3 -= 1
            p3, p4 = correção(p3, p4)
            if not tab[p3][p4] == '\U0001F538':
                break
            p3 += 1
        elif mov == 2:
            p4 += 1
            p3, p4 = correção(p3, p4)
            if not tab[p3][p4] == '\U0001F538':
                break
            p4 -= 1
        elif mov == 3:
            p4 -= 1
            p3, p4 = correção(p3, p4)
            if not tab[p3][p4] == '\U0001F538':
                break      
            p4 += 1
    g = len(rastrobot)
    while not g != tambot:
        i, j = rastrobot.pop(0) # retirando as posições antigas da lista
        tab[i][j] = '\U00002B1B' # substituindo as posições mais antigas do personagem por uma área vaga
        g += 1
    return [p3, p4]

def painel():
    painel = list("SNAKE'S SURVIVOR")
    for i in range(3):
        clear()
        print("\U0001F40D SNAKE'S SURVIVOR \U0001F40D")
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
    print("\U0001F40D SNAKE'S SURVIVOR \U0001F40D\n        Created by Douglas R. O. Silva \U0001F1E7 \U0001F1F7\n")

# declarações importantes e iniciais
clear = lambda: os.system('clear') # script para clear()
tab = [['\U00002B1B' for b in range(20)] for a in range(20)] # criando o tabuleiro usando list comprehesion
p1, p2, p3, p4, p5, p6 = 0, 0, 10, 10, 15, 15 # posição inicial do personagem
x = randint(0, 19) # sorteando a posição do primeiro alimento
y = randint(0, 19)
tam = 1 # tamanho inicial da cobra
tambot, tambot1 = 0, 0
a = 0 # iniciando o controle
rastro = [] # lista para guardar o rastro do personagem
rastrobot = [] # lista para guardar o rastro do personagem bot 
rastrobot1 = [] # lista para guardar o rastro do personagem bot 1
alimentos = ['\U0001F95A', '\U0001F35E', '\U0001F34A', '\U0001F352', '\U0001F34E', '\U0001F347', # ícones de alimentos
'\U0001F42D', '\U0001F430', '\U0001F400', '\U0001F430', '\U0001F425'] 
tab[x][y] = choice(alimentos) # alimento do personagem

clear()
painel()
print('Digite o número de bots que deseja colocar(0, 1 ou 2): ')
bots = int(readchar())
clear()
if bots == 1:
    p3, p4 = 14, 15
    tambot = 1
elif bots == 2:
    tambot, tambot1 = 1, 1
    p5, p6 = 9, 12
while True: # loop infinito
    tabuleiro(tab, p1, p2, p3, p4, p5, p6)
    for i in range(bots + 1):
        if i == 0:   
            player1(controlador(a)) 
            tab[p1][p2] = '\U0001F537' # posição atual do personagem 
        elif i == 1:
            [p3, p4] = bot(p3, p4, tambot, rastrobot)
            tab[p3][p4] = '\U0001F536' # posição atual do personagem bot
        elif i == 2:
            [p5, p6] = bot(p5, p6, tambot1, rastrobot1)
            tab[p5][p6] = '\U0001F536' # posição atual do personagem bot 
    clear()
