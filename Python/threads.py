'''
Este programa carrega uma lista de 100000 posições e substitui 26 dessas posições com o valor 'a'. Em seguida compara duas 
funções diferentes que utilizam essa mesma lista que procurar esses valores 'a', a primeira usa três threads enquanto a 
segunda realiza um for loop simples.
Ao final, cada função será executada 10000 vezes e será calculado o tempo de cada execução de 10000 vezes. Retornando estes tempos
ao usuário.

Saída:
Tempo com 3 threads: 23.882741224999336 segundos
Tempo sem threads: 64.79231731099935 segundos
'''

from threading import Thread
from random import randint
import timeit

lista = [num for num in range(99999)]

for a in range(26):
    lista[randint(0, 99998)] = 'a'

class Th(Thread):
    
        def __init__ (self, num, num2, cont):
            Thread.__init__(self)
            self.num = num
            self.num2 = num2
            self.cont = cont

        def run(self):
            for i in range(self.num, self.num2):
                if lista[i] == 'a':
                    self.cont += 1
                    
def caso_thread():
    
    global lista
    
    thread1 = Th(0, 33332, 0)
    thread1.start()

    thread2 = Th(333333, 66665, 0)
    thread2.start()

    thread3 = Th(666666, 99999, 0)
    thread3.start()

def caso_sem_thread():
    global lista
    contador = 0
    for i in range(len(lista)):
        if lista[i] == 'a':
            contador += 1
    

print(f'Tempo com 3 threads: {timeit.timeit(caso_thread, number=10000)}')
print(f'Tempo sem threads: {timeit.timeit(caso_sem_thread, number=10000)}')
