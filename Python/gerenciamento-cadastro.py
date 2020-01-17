'''
Este é um sistema de cadastro de pessoas pra uma certa festa sem restrições de idade 
'''

# necessário para clear() (limpar terminal) e sys.exit() (encerrar o programa)
import os # clear()
import sys #sys.exit()

#inicio do programa
clear = lambda: os.system('clear') # procedimento para clear()

# criando um dicionário com as pessoas da festa e contadores de dados
pessoas = {}
dados = {}.fromkeys('mulheres homens maioridade vip camarote pista'.split(), 0) # criando um dicionário com as palavras como key e todas com valor 0

# método de cadastro
def cadastrar():
    while True:
        clear()
        nome = input('Digite o nome: ')
        cpf = int(input('Digite o CPF: '))
        idade = int(input('Digite a idade: '))
        sexo = input('Digite o sexo: ')
        ingresso = input('Digite o tipo de ingresso (vip, camarote ou pista): ')
        clear()

        # confirmação de dados e reiteração do método, se desejado
        print(f'Nome: {nome.upper()}\nCPF: {cpf}\nIdade: {idade} anos\nSexo: {sexo.upper()}\nTipo de Ingresso: {ingresso.upper()}')        
        escolha = input('Deseja cadastrar (s/n)? ')
        if escolha == 's':
            pessoas[cpf] = [nome.upper(), idade, sexo.upper(), ingresso.upper()]

            # recolhendo dados necessário para consulta posterior
            if idade >= 18:
                dados['maioridade'] += 1
            if sexo == 'm':
                dados['homens'] += 1
            elif sexo == 'f':
                dados['mulheres'] += 1
            if ingresso == 'vip':
                dados['vip'] += 1
            elif ingresso == 'camarote':
                dados['camarote'] += 1
            elif ingresso == 'pista':
                dados['pista'] += 1
            # fim da coleta
            escolha = input('Deseja cadastrar outra pessoa (s/n)? ')
            if escolha == 'n':
                input('Sessão de cadastro encerrado com sucesso. Pressione Enter.')
                break
        else:
            escolha = input('Deseja reiniciar o cadastro (s/n)? ')
            if escolha == 'n':
                input('Sessão de cadastro encerrada com sucesso. Pressione Enter.')
                break 

# método de deleção de pessoas do cadastro
def deletar():
    while True:
        cpf = int(input('Digite o CPF da pessoa que deseja excluir: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, excluído
            print(f'Nome: {pessoas[cpf][0]}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}')
            escolha = input('Deseja mesmo excluir esta pessoa (s/n)? ')
            if escolha == 's':
                pessoas.pop(cpf)
                input('Pessoa removida com sucesso. Pressione Enter.')
                break
            else:
                input('Pessoa não excluída. Pressione Enter.')
                return
        else:
            print(f'O CPF: {cpf} não consta no cadastro.')
            escolha = input('Deseja reinserir o CPF (s/n)? ')
            if escolha == 'n':
                input('Sessão de deleção encerrada com sucesso. Pressione Enter.')
                break

def alterar():
    while True:
        cpf = int(input('Digite o CPF da pessoa que deseja alterar: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, editado
            print(f'Nome: {pessoas[cpf][0]}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}')
            escolha = input('Deseja mesmo editar esta pessoa (s/n)? ') 
            if escolha == 's':
# escolha do atributo a ser alterado
                escolha = input('Digite o que deseja editar (nome/cpf/idade/sexo/ingresso): ')
                if escolha == 'nome':
                    nome = input('Digite o novo nome: ')
                    pessoas[cpf][0] = nome.upper()
                    input('Nome alterado com sucesso. Pressione Enter.')
                    break
                elif escolha == 'cpf':
                    cpf2 = int(input('Digite o novo CPF: '))
                    pessoas[cpf2] = pessoas[cpf]
                    pessoas.pop(cpf)
                    input('CPF alterado com sucesso. Pressione Enter.')
                    break
                elif escolha == 'idade':
                    idade = int(input('Digite a nova idade: '))
                    pessoas[cpf][1] = idade
                    input('Idade editada com sucesso. Pressione Enter.')
                    break
                elif escolha == 'sexo':
                    ingresso = input('Digite o novo sexo: ')
                    pessoas[cpf][2] = sexo.upper()
                    input('Sexo editado com sucesso. Pressione Enter.')
                    break
                elif escolha == 'ingresso':
                    ingresso = input('Digite o novo ingresso: ')
                    pessoas[cpf][3] = ingresso.upper()
                    input('ingresso editado com sucesso. Pressione Enter.')
                    break
                else:
                    input('Não foi encontrado o atributo inserido. Pressione Enter.')
                    break
            else:
                input('Pessoa não editada. Pressione Enter.')
                return
        else:
            print(f'O CPF: {cpf} não consta no cadastro.')
            escolha = input('Deseja reinserir o CPF (s/n)? ')
            if escolha == 'n':
                input('Sessão de deleção encerrada com sucesso. Pressione Enter.')
                break

# método para consultar pessoas no cadastro e outras informações 
def consultar():
    escolha = int(input('1 - Cadastros\n2 - Número de cadastrados\n3 - Consulta específica\nDigite uma das opções acima: '))
    if escolha == 1:
        clear()
        for cpf in pessoas.keys():
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}\n')
        input('Pressione Enter para retornar ao gerenciamento.')
    elif escolha == 2:
        clear()
        print(f"QUANTIDADES\nPessoas cadastradas: {len(pessoas)}\nMaiores de idade: {dados['maioridade']}\nHomens: {dados['homens']}")
        print(f"Mulheres: {dados['mulheres']}\nVIP: {dados['vip']}\nCamarote: {dados['camarote']}\nPista: {dados['pista']}")
        input('Pressione Enter para retornar ao gerenciamento.')
    elif escolha == 3:
        clear()
        cpf = int(input('Digite o CPF: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, editado
            clear()
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}')
            input('Fim da consulta. Pressione Enter.')
        else:
            input('Este CPF não consta no cadastro. Pressione Enter.')

# programa principal
while True: # loop infito para retorno do painel principal
    clear()
    print('Bem vindo, ao gerenciamento de pessoas ao evento XYZ.')
    escolha = int(input('1 - Cadastrar\n2 - Deletar\n3 - Alterar\n4 - Consultar\n5 - Encerrar Sistema\nDigite uma das opções acima: '))
    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        deletar()
    elif escolha == 3:
        alterar()
    elif escolha == 4:
        consultar()
    elif escolha == 5:
        sys.exit() # mantido aqui para fins didáticos, mas ele é completamente desnecessário, retirá-lo implica no mesmo resultado
    else:
        input('Digite uma das opções acima. Pressione Enter.')


