'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
'''
# importanto os para clear
import os 

def votacao(nome, i):
    global lista
    print(f'O Sistema Operacional mais votado foi o {nome}, com {lista.count(i)} votos, correspondendo a {int(lista.count(i)*100/len(lista))}% dos votos.')

# criando o painel

def painel():
    print('VOTAÇÃO DE MELHOR OS')
    print('1 - Windows\n2 - Unix\n3 - Linux\n4 - Netware\n5 - MacOS\n6 - Outro\n0 - Sair')

# renomeando a função os.system('clear') para clear()
clear = lambda: os.system('clear')

# criando a lista de valores
lista = []

# loop infinito e votação
while True:
    clear()
    painel()
    print('Digite um dos valores acima: ', end='')
    escolha = int(input())
    if escolha == 1:
        lista.append(1)
    elif escolha == 2:
        lista.append(2)
    elif escolha == 3:
        lista.append(3)
    elif escolha == 4:
        lista.append(4)
    elif escolha == 5:
        lista.append(5)
    elif escolha == 6:
        lista.append(6)
    elif escolha == 0:
        break
    else:
        print('Não é possível outros valores além dos listados. Presione ENTER.', end = '')
        input()

# fornecendo os resultados
print(f'\nRESULTADO Total de votos {len(lista)}.\n ')

# definindo o vencedor
i = 1
vencedor = []
while i <=6:
    vencedor.append(lista.count(i))
    i += 1
i = vencedor.index(max(vencedor)) + 1
# fornecendo o resultado
if i == 1:
    votacao('Windows', 1)
elif i == 2:
    votacao('Unix', 2)
elif i == 3:
    votacao('Linux', 3)
elif i == 4:
    votacao('Netware', 4)
elif i == 5:
    votacao('MacOS', 5)
else:
    votacao('Outros', 6)
