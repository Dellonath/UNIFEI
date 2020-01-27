# FUNÇÕES QUE PODEM SER MUITO ÚTEIS
####################################################################
'''
Esta é a função readchar(), ela é capaz de executar uma espécie de input() mas sem que seja necessário pressionar enter
'''
import sys # necessário importar esta biblioteca 
import tty # necessário importar esta biblioteca 
import termios # necessário importar esta biblioteca S

def readchar(): # esta é a implementação do readchar() no Linux, é necessário adicioná-la no programa
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

a = readchar() # qualquer tecla digitada no teclado será automaticamente guardado na variável 'a'

####################################################################
'''
Esta função é capaz de limpar o console
'''
import os # necessário importar esta biblioteca

clear = lambda: os.system('clear') # script para clear()

clear() # chamando a função para limpar o console

####################################################################
'''
Esta função é capaz de manter selecionado uma tecla até sua liberação, é como se eu mantesse pressionado a tecla
'''
from pynput.keyboard import Key, Controller # necessário importar esta biblioteca

keyboard = Controller() # aqui eu estou definindo a variável keyboard como uma instância do Controller

keyboard.press('a') # aqui é como se eu mantivesse a tecla 'a' pressionada

keyboard.release('a') # aqui é como se eu liberasse a tecla 'a' 

####################################################################

