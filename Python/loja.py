'''
Desenvolvimento de um sistema rápido de compras para a onMarket, optei por realizar este tipo de 'árvore' entre as funções para fins didáticos e para aperfeiçoamento do nível lógico
'''
 
# 'import os' para clear() e exit 
import os
import sys #sys.exit()
clear = lambda: os.system('clear') # necessário para clear()

car = [] # declarando o carrinho 

produtos = { # declarando os produtos da loja
'playstation': [1900.00, 'Sony', 2], 
'tênis': [299.99, 'Nike', 3], 
'stronghold': [74.99, 'Firefly Studios', 3],
'camiseta': [14.99, 'Ecko', 2],
'calça': [39.99, 'Ecko', 1],
'notebook': [1799.99, 'ASUS', 2],
'bicicleta': [399.99, 'Cornodale', 2],
'smartphone': [799.99, 'Samsung', 2],
'pizza': [9.99, 'Sadia', 3],
'lasanha': [7.99, 'Sadia', 4],
'brinquedo': [14.99, 'Estrela', 2],
'pão': [0.69, 'Padaria Bom Gosto', 70],
'carro': [29999.99, 'Chevrolet', 1],
'cesta': [69.99, 'Padaria Bom Gosto', 3],
'computador': [1299.99, 'Samsung', 1],
'placa-mãe': [399.99, 'ASUS', 2]
}

def painel(): # método para saída de produtos
    print('____________________________________________________\n')
    print('Bem-vindo ao onMarket, boas compras!!! :D')
    print('____________________________________________________\n\n')
    for prod in produtos.keys():
        print(f'\nNome: {prod.capitalize()}\nMarca: {produtos[prod][1]}\nQuantidade Disponivel: {produtos[prod][2]}\nR${produtos[prod][0]}')
    print('\n')

def compra():
    painel()
    prod = input("\nDigite o nome do produto que deseja comprar. Digite 'lista' para acessar o carrinho e 'sair' para encerrar as compras: ").lower()
    clear()
    if prod == 'lista': # acesso rápido à lista
        carrinho()
        clear()
    elif prod == 'sair':
        input('Compras finalizadas. Muito obrigado. :) ')
        sys.exit()
    else:
        if prod in produtos.keys() and produtos[prod][2] != 0:
            print(f'Nome: {prod.capitalize()}\nMarca: {produtos[prod][1]}\nQuantidade Disponivel: {produtos[prod][2]}\nPreço: {produtos[prod][0]}')
            escolha = input('\nDeseja mesmo comprar este produto (s/n)? ')
            if escolha == 's': # confirmação de compra
                qtd = int(input('Insira a quantidade desejada: '))
                while produtos[prod][2] - qtd < 0: # verificação de quantidade
                    clear()
                    print(f'Não é possível efetuar a compra. O número desejado supera o disponível. Tente um valor mais baixo (até {produtos[prod][2]} unidades): ')
                    qtd = int(input('Insira a quantidade desejada: '))
                car.append([prod, produtos[prod][1], produtos[prod][0], qtd]) # adicionando produto ao carrinho               
                produtos[prod][2] = produtos[prod][2] - qtd # retirando quantidade comprada do estoque
                if prod[-1::] == 'a': # a estrutura condicional abaixo trata-se apenas para concordância literal. prod[-1::] implica no retorno do último caracter da string prod
                    clear()
                    input(f"Produto comprado com sucesso, obrigado, aproveite sua nova {prod}. Pressione Enter para retornar às compras. :) ")
                else:
                    clear()
                    input(f"Produto comprado com sucesso, obrigado, aproveite seu novo {prod}. Pressione Enter para retornar às compras. :) ")
            else:
                clear()
                input("Ah, é uma pena, mas temos outros produtos, aproveite. :)")
        else:
            clear()
            input('Este produto não encontra-se disponível no momento. Mas temos outras opções. Pressione Enter.')

def carrinho(): # método para consulta e exclusão de itens no carrinho
    clear()
    print('1 - Ver lista\n2 - Comprar produto\n3 - Retirar produto')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        clear()
        if len(car) == 0:
            clear()
            input('Lista Vazia. Pressione Enter.')
            return
        else:
            clear()
            for prod in car:
                print(f'Nome: {prod[0].capitalize()}\nMarca: {prod[1]}\nQuantidade: {prod[3]}\nPreço: {prod[2]}\n')
            print(f'\nNúmero de produtos: {len(car)}')
            soma = 0
            for i in range(len(car)):
                soma = soma + car[i][2]*car[i][3]
            print(f'Gasto total: {round(soma, 5)}')
            input('\nFim do carrinho. Pressione Enter.')
    elif escolha == 2:
        clear()
        compra()
    elif escolha == 3:
        prod = input('Digite o nome do produto que deseja retirar da lista: ')
        clear()
        for i in range(len(car)):
            if car[i][0] == prod:
                print(f'Nome: {car[i][0].capitalize()}\nMarca: {car[i][1]}\nQuantidade: {car[i][3]}\nPreço: {car[i][2]}\n')
                escolha = input('Deseja mesmo retirar este produto? ')
                if escolha == 's':
                    car.pop(i)
                    input('Produto retirado com sucesso. Pressione Enter.')
                else:
                    input('Produto mantido. Pressione Enter.')
                break

while True:
    compra()