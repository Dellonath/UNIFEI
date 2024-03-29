'''
Jogo da velha
'''

import time # import para time.sleep()
import os # import para clear()
import sys

clear = lambda: os.system('clear') # script para clear()

def painel(): # função desnecessária, apenas para usar o time.sleep() de uma forma diferente e guardar a sintaxe do mesmo
    clear()
    for a in range(3):
        print('JOGO DA VELHA')
        time.sleep(0.5) # não é necessário inserir um timer, deixei-o aqui para posterior consulta na sintaxe e uso em outros sistemas
        clear()
        time.sleep(0.5)

def tabuleiro(tab): # função apenas para imprimir o tabuleiro atual
    c = 0
    print('   0  1  2')
    for i in tab:
        print(c, end = '')
        c += 1
        print(end = ' ')
        for a in i:
            print(a, end = ' ')
        print()
    print()

def jog1(): # método para vitória do jogar 1
    clear()
    global cont # tomando o cont global
    global tab # tomando o tab global
    tabuleiro(tab)
    a = input('JOGADOR 1 VENCEU O JOGO!!! Jogar novamente (s/n)? ')
    if a == 's':
        cont = 0
        tab = [['\U00002B1B' for i in range(3)] for num in range(3)] # reiniciando o tabuleiro
        clear()
    else:
        clear()
        input('Programa finalizado. Pressione Enter.')
        sys.exit()

def jog2():
    clear()
    global cont # tomando o cont global
    global tab # tomando o tab global
    tabuleiro(tab)
    a = input('JOGADOR 2 VENCEU O JOGO!!! Jogar novamente (s/n)? ')
    if a == 's':
        cont = 0
        tab = [['\U00002B1B' for i in range(3)] for num in range(3)] # reiniciando o tabuleiro
        clear()
    else:
        clear()
        input('Programa finalizado. Pressione Enter.')
        sys.exit()

def verificador(tab): 
# método para verificação de vitória, separei em vários elif's para não ter uma única operação lógica imensa, contém todas as possibilidades de vitória
    if tab[0][0] == tab[0][1] == tab[0][2] == '\U0001F537' or tab[1][0] == tab[1][1] == tab[1][2] == '\U0001F537': # duas primeiras colunas 
        jog1()
    elif tab[0][0] == tab[1][0] == tab[2][0] == '\U0001F537' or tab[0][0] == tab[1][0] == tab[2][0] == '\U0001F537': # terceira coluna e primeira linha 
        jog1()
    elif tab[0][1] == tab[1][1] == tab[2][1] == '\U0001F537' or tab[0][2] == tab[1][2] == tab[2][2] == '\U0001F537': # duas últimas linhas
        jog1()
    elif tab[0][0] == tab[1][1] == tab[2][2] == '\U0001F537' or tab[0][2] == tab[1][1] == tab[2][0] == '\U0001F537': # diagonais
        jog1()
    elif tab[0][0] == tab[0][1] == tab[0][2] == '\U0001F536' or tab[1][0] == tab[1][1] == tab[1][2] == '\U0001F536': 
        jog2()
    elif tab[0][0] == tab[1][0] == tab[2][0] == '\U0001F536' or tab[0][0] == tab[1][0] == tab[2][0] == '\U0001F536': 
        jog2()
    elif tab[0][1] == tab[1][1] == tab[2][1] == '\U0001F536' or tab[0][2] == tab[1][2] == tab[2][2] == '\U0001F536': 
        jog2()
    elif tab[0][0] == tab[1][1] == tab[2][2] == '\U0001F536' or tab[0][2] == tab[1][1] == tab[2][0] == '\U0001F536': 
        jog2()


# PROGRAMA PRINCIPAL

tab = [['\U00002B1B' for i in range(3)] for num in range(3)] # declarando o tabuleiro, usando List Comprehension

painel() 
print('O jogo funciona da seguinte forma: as posições variam de 0 a 2, sendo 0 a primeira posição e 2 a última posição da linha ou coluna.', end = ' ')
input("Primeiro você escolherá a posição na coluna, em seguida a posição na linha. Os locais com \U00002B1B indicam as posições vazias. Pressione Enter.")

cont = 0 # contador de jogadas
while True:
    verificador(tab)
    clear()
    if cont % 2 == 0: # vez do jogador 1
        tabuleiro(tab)
        print(f"Jogador 1, digite onde deseja marcar o \U0001F537 (rodada {cont}): ", end = ' ')
        a = int(input())
        if not 0 <= a <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
            while True:
                clear()
                tabuleiro(tab)
                print('Jogador 1, digite um número entre 0 e 2, inclusive: ', end = ' ')
                a = int(input())
                if 0 <= a <= 2:
                    break
        b = int(input())
        if not 0 <= b <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
            while True:
                clear()
                tabuleiro(tab)
                print(f'Valor anterior: {a}')
                print('Jogador 1, digite um número entre 0 e 2, inclusive: ', end = ' ')   
                b = int(input())
                if 0 <= b <= 2:
                    break

        if tab[b][a] == '\U0001F537' or tab[b][a] == '\U0001F536': # verificando se a posição escolhida já foi ocupada
            while True:
                clear()
                tabuleiro(tab)
                print('Jogador 1, esta posição já está ocupada, digite outra posição: ', end = ' ')
                a = int(input())
                if not 0 <= a <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar KeyError
                    while True:
                        clear()
                        tabuleiro(tab)
                        print('Jogador 1, digite um número entre 0 e 2, inclusive: ', end = ' ')
                        a = int(input())
                        if 0 <= a <= 2:
                            break
                b = int(input())
                if tab[b][a] == '\U00002B1B': # se a vaga estiver não preenchida
                    break
        tab[b][a] = '\U0001F537'
    else: # vez do jogador 2
        tabuleiro(tab)
        print(f"Jogador 2, digite onde deseja marcar o \U0001F536 (rodada {cont}): ", end = ' ')
        a = int(input())
        if not 0 <= a <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
            while True:
                clear()
                tabuleiro(tab)
                print('Jogador 2, digite um número entre 0 e 2, inclusive: ', end = ' ')
                a = int(input())
                if 0 <= a <= 2:
                    break
        b = int(input())
        if not 0 <= b <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
            while True:
                clear()
                tabuleiro(tab)
                print(f'Valor anterior: {a}')
                print('Jogador 2, digite um número entre 0 e 2, inclusive: ', end = ' ')
                b = int(input())
                if 0 <= b <= 2:
                    break
        if not 0 <= b <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
            while True:
                clear()
                tabuleiro(tab)
                print(f'Valor anterior: {a}')
                print('Jogador 2, digite um número entre 0 e 2, inclusive: ', end = ' ')
                b = int(input())
                if 0 <= b <= 2:
                    break
        if tab[b][a] == '\U0001F537' or tab[b][a] == '\U0001F536': # verificando se a posição escolhida já foi ocupada
            while True:
                clear()
                tabuleiro(tab)
                print('Jogador 2, esta posição já está ocupada, digite outra posição: ', end = ' ')
                a = int(input())
                if not 0 <= a <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar KeyError
                    while True:
                        clear()
                        tabuleiro(tab)
                        print('Jogador 2, digite um número entre 0 e 2, inclusive: ', end = ' ')
                        a = int(input())
                        if 0 <= a <= 2:
                            break
                b = int(input())
                if not 0 <= b <= 2: # verificar se a posição varia entre 0 e 2, inclusive, para evitar keyerror
                    while True:
                        clear()
                        tabuleiro(tab)
                        print(f'Valor anterior: {a}')
                        print('Jogador 2, digite um número entre 0 e 2, inclusive: ', end = ' ')
                        b = int(input())
                        if 0 <= b <= 2:
                            break
                if tab[b][a] == '\U00002B1B': # se a vaga estiver não preenchida
                    break
        tab[b][a] = '\U0001F536'
    clear()
    cont += 1

    if cont == 9: # finaliza no número máximo de jogadas
        clear()
        tabuleiro(tab)
        a = input('EMPATE!!! Jogar novamente (s/n)? ')
        if a == 's':
            cont = 0
            tab = [['\U00002B1B' for i in range(3)] for num in range(3)]
        else:
            break
