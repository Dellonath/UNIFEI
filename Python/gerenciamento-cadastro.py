'''
Este é um sistema de cadastro de pessoas pra uma certa festa sem restrições de idade 
'''

# necessário para clear() (limpar terminal) e sys.exit() (encerrar o programa)
import os # clear()
import sys #sys.exit()
from csv import DictReader, writer

clear = lambda: os.system('clear') # função para clear()
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
            with open('cadastros.csv', 'a') as arquivo: # adicionando dados à cadastros.csv
                escritor_csv = writer(arquivo)
                escritor_csv.writerow([nome.upper(), cpf, sexo.upper(), idade, ingresso.upper()])  
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
    clear()
    while True:
        cpf = int(input('Digite o CPF da pessoa que deseja excluir: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, excluído
            clear()
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}\n')
            escolha = input('Deseja mesmo excluir esta pessoa (s/n)? ')
            if escolha == 's':
                if int(pessoas[cpf][1]) >= 18:
                    dados['maioridade'] -= 1
                if pessoas[cpf][2] == 'M':
                    dados['homens'] -= 1
                elif pessoas[cpf][2] == 'F':
                    dados['mulheres'] -= 1
                if pessoas[cpf][3] == 'VIP':
                    dados['vip'] += 1
                elif pessoas[cpf][3] == 'CAMAROTE':
                    dados['camarote'] += 1
                elif pessoas[cpf][3] == 'PISTA':
                    dados['pista'] += 1
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
    clear()
    while True:
        cpf = int(input('Digite o CPF da pessoa que deseja alterar: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, editado
            clear()
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}\n')
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
    clear()
    escolha = int(input('1 - Cadastros\n2 - Número de cadastrados\n3 - Consulta específica\nDigite uma das opções acima: '))
    if escolha == 1:
        clear()
        for cpf in pessoas.keys():
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}\n')
        input('Pressione Enter para retornar ao gerenciamento.')
    elif escolha == 2:
        clear()
        print(f"QUANTIDADES\nPessoas cadastradas: {len(pessoas)}\nMaiores de idade: {dados['maioridade']}\nHomens: {dados['homens']}")
        print(f"Mulheres: {dados['mulheres']}\nVIP: {dados['vip']}\nCamarote: {dados['camarote']}\nPista: {dados['pista']}\n")
        input('Pressione Enter para retornar ao gerenciamento.')
    elif escolha == 3:
        clear()
        cpf = int(input('Digite o CPF: '))
        if cpf in pessoas.keys(): # verificação se há ou não o cadastro do cpf, caso True será, após confirmação, editado
            clear()
            print(f'Nome: {pessoas[cpf][0]}\nCPF: {cpf}\nIdade: {pessoas[cpf][1]}\nSexo: {pessoas[cpf][2]}\nTipo de Ingresso: {pessoas[cpf][3]}\n')
            input('Fim da consulta. Pressione Enter.')
        else:
            input('Este CPF não consta no cadastro. Pressione Enter.')

# programa principal

try:
    with open('cadastros.csv') as arquivo: # recuperando dados em arquivo csv, caso o arquivo não exista, ele o cria com cabeçalho
        leitor_csv = DictReader(arquivo)
        for arq in leitor_csv:
            pessoas[int(arq['cpf'])] = [arq['nome'].upper(), arq['idade'].upper(), arq['sexo'].upper(), arq['ingresso'].upper()]
            if int(arq['idade']) >= 18:
                dados['maioridade'] += 1
            if arq['sexo'] == 'M':
                dados['homens'] += 1
            elif arq['sexo'] == 'F':
                dados['mulheres'] += 1
            if arq['ingresso'] == 'VIP':
                dados['vip'] += 1
            elif arq['ingresso'] == 'CAMAROTE':
                dados['camarote'] += 1
            elif arq['ingresso'] == 'PISTA':
                dados['pista'] += 1
except:
    with open('cadastros.csv', 'w') as arquivo: # criando arquivo com cabeçalho
        escritor_csv = writer(arquivo)
        escritor_csv.writerow(['nome', 'cpf', 'sexo', 'idade', 'ingresso'])

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
        with open('cadastros.csv', 'w') as arquivo: # atualiza o arquivo csv
            escritor_csv = writer(arquivo)
            escritor_csv.writerow(['nome', 'cpf', 'sexo', 'idade', 'ingresso'])
            for i in pessoas.keys():
                escritor_csv.writerow([pessoas[i][0], i, pessoas[i][2], pessoas[i][1], pessoas[i][3]])    
        print(pessoas)
        sys.exit() # mantido aqui para fins didáticos, mas ele é completamente desnecessário, retirá-lo implica no mesmo resultado
    else:
        input('Digite uma das opções acima. Pressione Enter.')

