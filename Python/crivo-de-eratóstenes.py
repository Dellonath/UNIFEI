'''
Crie o Crivo de Eratóstenes e imprima-o
'''
primos=[2, 3, 5, 7]
lista=list(range(8, 101)) #lista de 8 a 100, não de 1 pois o if vai retirar o 2, 3, 5, 7
i=8
while i<101:
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:  #verifica número a número e verifica se 2, 3, 5 ou 7 divide-o
    	lista.pop(lista.index(i))
    i+=1
lista=primos+lista #concatenando as duas listas
print(f'CRIVO DE ERATÓSTENES\n{lista}')
