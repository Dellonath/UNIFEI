import os  # import para os.system('clear')
import time  # import para time.sleep()
from passlib.hash import pbkdf2_sha256 as cryp # import para criptografia de senhas
from colorama import Fore, Style, init # import para fontes coloridas
import sys # necessário importar para readchar().upper() 
import tty # necessário importar para readchar().upper() 
import termios # necessário importar para readchar().upper()
from datetime import datetime # usado para datetime.now() para informar a data atual

def readchar(): # esta é a implementação do readchar().upper(), esta função cumpre a função do input() mas sem exigir a tecla Enter
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def painel_apresentacao():
    print(Style.BRIGHT + Fore.CYAN + 'BEM-VINDO AO ACADY')
    print(Style.BRIGHT + Fore.CYAN + 'O seu banco amigo\n')
    print('Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print('1 - Login.')
    print('2 - Sair.\n')
    return readchar().upper()

def painel_cliente(cliente):
    print(Style.BRIGHT + Fore.CYAN + f'Olá, {cliente.nome} {cliente.sobrenome}, bem-vindo à sua ACADY Account.')
    print(Fore.CYAN + 'CLIENTE')
    print(Fore.CYAN + "Lembre-se de utilizar apenas 's' para SIM e 'n' para NÃO.\n")
    print('Abaixo há algumas opções, pressione o que você deseja fazer:')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Transferir')
    print('4 - Consultar extrato/saldo')
    print('5 - Consultar informações')
    print('6 - Sair')
    return readchar().upper()

def painel_colaborador_cx(colaborador):
    print(Style.BRIGHT + Fore.CYAN + f'Olá, {colaborador.nome} {colaborador.sobrenome}, bem-vindo à sua ACADY CX Manager Account.')
    print(Fore.CYAN + 'COLABORADOR CAIXA')
    print(Fore.CYAN + "Lembre-se de utilizar apenas 's' para SIM e 'n' para NÃO.\n")
    print('Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print('1 - Criar cliente')
    print('2 - Remover cliente ')
    print('3 - Consultar cliente')
    print('4 - Alterar cliente')
    print('5 - Sair ')
    return readchar().upper()

def painel_colaborador_rh(colaborador):
    print(Style.BRIGHT + Fore.CYAN + f'Olá, {colaborador.nome} {colaborador.sobrenome}, bem-vindo à sua ACADY RH Manager Account.')
    print(Fore.CYAN + 'COLABORADOR RH')
    print(Fore.CYAN + "Lembre-se de utilizar apenas 's' para SIM e 'n' para NÃO.\n")
    print('Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print('1 - Criar funcionário')
    print('2 - Remover funcionário ')
    print('3 - Consultar funcionário')
    print('4 - Alterar funcionário')
    print('5 - Sair ')
    return readchar().upper()

def obrigatorio(arg): # verifica se o arg é vazio
    if arg == '':
        clear()
        print('Este campo é obrigatório.')
        time.sleep(2)
        clear()
        return False
    return True

def conta_colaborador_cx(colaborador, bd):
    while True:
        clear()
        a = painel_colaborador_cx(colaborador)
        if a == '1':
            clear()
            print('Área de registro de novo Cliente ACADY.') 
            print('Abaixo, insira os dados do cliente: \n')
            while True:
                nome = input('Digite o Nome: ').title()
                if Pessoa.apenas_letras(nome) and obrigatorio(nome):
                    break
            while True:
                sobrenome = input('Digite o Sobrenome: ').title()
                if Pessoa.apenas_letras(sobrenome) and obrigatorio(sobrenome):
                    break
            while True:
                cpf = input('Digite o CPF: ')
                d = True
                if obrigatorio(cpf):
                    for client in bd.values():
                        if cpf == client.cpf:
                            clear()
                            print('Este CPF já foi cadastrado.')
                            time.sleep(2)
                            clear()
                            d = False
                            break
                    if d and Pessoa.apenas_numeros(cpf):
                        break
            while True:
                idade = input('Digite a Idade: ')
                if obrigatorio(idade) and Pessoa.apenas_numeros(idade):
                    break
            while True:
                sexo = input('Digite o Sexo: ').upper()
                if sexo == 'M' or sexo == 'F':
                    break
                clear()
                print("Digite 'm' ou 'f' para o sexo do cliente.")
                time.sleep(2)
                clear()
            while True:
                clear()
                endereco = input('Digite a Cidade: ').title()
                if obrigatorio(endereco) and Pessoa.apenas_letras(endereco):
                    break
            while True:
                telefone = input('Digite o Telefone: ')
                if obrigatorio(telefone) and Pessoa.apenas_numeros(telefone):
                    break
            while True:
                clear()
                login = input('Digite o Login: ')
                if obrigatorio(login) and login in bd.keys():
                    clear()
                    print('Este login já foi cadastrado.')
                    time.sleep(2)
                if obrigatorio(login) and not login in bd.keys():
                    break
            while True:
                clear()
                senha = input('Digite a Senha: ')
                if senha:
                    break
                else:
                    clear()
                    print('Campo obrigatório.')
                    time.sleep(2)
            while True:
                clear()
                renda = input('Digite a Renda Inicial: ')
                if obrigatorio(renda) and Pessoa.apenas_numeros(renda):
                    renda = int(renda)
                    break
            while True:
                clear()
                limite = input('Digite o Limite Inicial: ')
                if obrigatorio(limite) and Pessoa.apenas_numeros(limite):
                    limite = int(limite)
                    break
            while True:
                clear()
                saldo = input('Digite o Saldo Inicial: ')
                if obrigatorio(saldo) and Pessoa.apenas_numeros(saldo):
                    saldo = int(saldo)
                    break          
            while True:
                clear()
                print('Dados do novo Cliente ACADY: \n')
                print(f'Nome: {nome}')
                print(f'Sobrenome: {sobrenome}')
                print(f'CPF: {cpf}')
                print(f'Idade: {idade}')
                print(f'Sexo: {sexo}')
                print(f'Endereço: {endereco}')
                print(f'Telefone: +55 035 {telefone}')
                print(f'Login: {login}')
                print(f'Senha: ************')
                print(f'Renda: {renda}')
                print(f'Saldo: {saldo}')
                print(f'Limite: {limite}\n')
                print('Deseja mesmo cadastrar este cliente (s/n): ')
                a = readchar().upper()
                if a == 'S':
                    try:
                        bd[login] = Cliente(nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha, renda, limite, saldo)
                    except:
                        clear()
                        print('Não foi possível efetuar o cadastro.')
                        time.sleep(2)
                        break
                    clear()
                    print('O cliente foi cadastrado com sucesso.')
                    time.sleep(2)
                    break
                elif a == 'N':
                    clear()
                    print('Operação cancelada. Os dados foram apagados com sucesso.')
                    time.sleep(2)
                    break
                else:
                    clear()
                    print('Comando não reconhecido. Os dados foram apagados.')
                    time.sleep(2)
        elif a == '2':
            clear()
            login = input('Digite o Login do cliente que deseja remover: ')
            if obrigatorio(login) and login in bd.keys():
                cliente = bd[login]
                a = True
            else:
                clear()
                print('Este login não está cadastrado.')
                time.sleep(2)
            if a:
                clear()
                print('Dados do Cliente ACADY: \n')
                print(f'Nome: {cliente.nome}')
                print(f'Sobrenome: {cliente.sobrenome}')
                print(f'CPF: {cliente.cpf}')
                print(f'Idade: {cliente.idade}')
                print(f'Sexo: {cliente.sexo}')
                print(f'Endereço: {cliente.endereco}')
                print(f'Telefone: {cliente.telefone}')
                print(f'Login: {cliente.login}')
                print(f'Senha: ************')
                print(f'Conta: {cliente.conta}')
                print(f'Renda: {cliente.renda}')
                print(f'Saldo: {cliente.saldo}')
                print(f'Limite: {cliente.limite}\n')
                print('Deseja mesmo remover este Cliente (s/n): ')
                a = readchar().upper()
                if a == 'S':
                    bd.pop(login)
                    clear()
                    print('A conta foi apagada com sucesso.')
                    time.sleep(2)
                    clear()
                elif a == 'N':
                    clear()
                    print('Operação cancelada.')
                    time.sleep(2)
                    clear()
                else:
                    clear()
                    print('Comando não reconhecido. A conta não foi removida.')
                    time.sleep(2)
        elif a == '3':
            clear()
            login = input('Digite o Login do cliente que deseja consultar: ')
            clear()
            if obrigatorio(login) and login in bd.keys():
                cliente = bd[login]
                a = True
            else:
                clear()
                print('Este login não está cadastrado.')
                a = False
                time.sleep(2)
            if a:
                print('Dados do Cliente ACADY consultado: \n')
                print(f'Nome: {cliente.nome}')
                print(f'Sobrenome: {cliente.sobrenome}')
                print(f'CPF: {cliente.cpf}')
                print(f'Idade: {cliente.idade}')
                print(f'Sexo: {cliente.sexo}')
                print(f'Endereço: {cliente.endereco}')
                print(f'Telefone: {cliente.telefone}')
                print(f'Login: {cliente.login}')
                print(f'Senha: ************')
                print(f'Conta: {cliente.conta}')
                print(f'Renda: {cliente.renda}')
                print(f'Saldo: {cliente.saldo}')
                print(f'Limite: {cliente.limite}\n')
                input('Pressione Enter para sair. ')
        elif a == '4':
            clear()
            login = input('Digite o Login do cliente que deseja alterar: ')
            clear()
            if obrigatorio(login) and login in bd.keys():
                cliente = bd[login]
                a = True
            else:
                clear()
                print('Este login não está cadastrado.')
                time.sleep(2)
                a = False
                clear()
            if a:
                print('Dados do Cliente ACADY: \n')
                print(f'Nome: {cliente.nome}')
                print(f'Sobrenome: {cliente.sobrenome}')
                print(f'CPF: {cliente.cpf}')
                print(f'Idade: {cliente.idade}')
                print(f'Sexo: {cliente.sexo}')
                print(f'Endereço: {cliente.endereco}')
                print(f'Telefone: {cliente.telefone}')
                print(f'Login: {cliente.login}')
                print(f'Senha: ************')
                print(f'Conta: {cliente.conta}')
                print(f'Renda: {cliente.renda}')
                print(f'Saldo: {cliente.saldo}')
                print(f'Limite: {cliente.limite}\n')
                a = input('Digite o dado que deseja alterar: ').upper()
                if a == 'NOME':
                    clear()
                    nome = input('Digite um Nome: ').title()
                    if Pessoa.apenas_letras(nome):
                        clear()
                        print(f'Nome alterado de {cliente.nome} para {nome} com sucesso.')
                        time.sleep(2)
                        cliente.nome = nome
                        clear()
                elif a == 'SOBRENOME':
                    clear()
                    sobrenome = input('Digite um Sobrenome: ').title()
                    if Pessoa.apenas_letras(sobrenome):
                        clear()
                        print(f'Sobrenome alterado de {cliente.sobrenome} para {sobrenome} com sucesso.')
                        time.sleep(2)
                        cliente.sobrenome = sobrenome
                        clear()
                elif a == 'CPF':
                    clear()
                    cpf = input('Digite um CPF: ')
                    if obrigatorio(cpf) and Pessoa.apenas_numeros(cpf):
                        clear()
                        print(f'CPF alterado de {cliente.cpf} para {cpf} com sucesso.')
                        time.sleep(2)
                        cliente.cpf = cpf
                        clear()
                elif a == 'Idade':
                    clear()
                    idade = input('Digite uma Idade: ')
                    if obrigatorio(idade) and Pessoa.apenas_numeros(idade):
                        clear()
                        print(f'Idade alterada de {cliente.idade} para {idade} com sucesso.')
                        time.sleep(2)
                        cliente.idade = idade
                        clear()
                elif a == 'SEXO':
                    clear()
                    sexo = input('Digite um Sexo: ').upper()
                    if sexo == 'F' or sexo == 'M':
                        clear()
                        print(f'Sexo alterado de {cliente.sexo} para {sexo} com sucesso.')
                        time.sleep(2)
                        cliente.sexo = sexo
                        clear()
                    else:
                        clear()
                        print('Sexo não reconhecido. Operação cancelada.')
                        time.sleep(2)
                        clear()
                elif a == 'ENDEREÇO':
                    clear()
                    endereco = input('Digite um Endereço: ').title()
                    if obrigatorio(endereco) and Pessoa.apenas_letras(endereco):
                        clear()
                        print(f'Endereço alterado de {cliente.endereco} para {endereco} com sucesso.')
                        time.sleep(2)
                        cliente.endereco = endereco
                        clear()
                elif a == 'TELEFONE':
                    clear()
                    telefone = input('Digite um Telefone: ').title()
                    if obrigatorio(telefone) and Pessoa.apenas_numeros(telefone):
                        clear()
                        print(f'Telefone alterado de {cliente.telefone} para +55 035 {telefone} com sucesso.')
                        time.sleep(2)
                        cliente.telefone = telefone
                        clear()
                elif a == 'LOGIN':
                    clear()
                    login = input('Digite um Login: ')
                    if obrigatorio(login):
                        clear()
                        print(f'Login alterado de {cliente.login} para {login} com sucesso.')
                        bd.pop(cliente.login)
                        bd[login] = cliente
                        time.sleep(2)
                        cliente.login = login
                        clear()
                elif a == 'SENHA':
                    clear()
                    if obrigatorio(senha):
                        senha = input('Digite uma Senha: ')
                        clear()
                        print(f'Senha alterada com sucesso.')
                        time.sleep(2)
                        cliente.senha = senha
                        clear()
                elif a == 'CONTA':
                    clear()
                    print('O dado Conta não pode ser alterado.')
                    time.sleep(2)
                    clear()
                elif a == 'RENDA':
                    clear()
                    renda = input('Digite um valor para Renda: ')
                    if obrigatorio(renda) and Pessoa.apenas_numeros(renda):
                        clear()
                        print(f'Renda alterada de {cliente.renda} para {renda} com sucesso.')
                        time.sleep(2)
                        cliente.renda = int(renda)
                        clear()
                elif a == 'SALDO':
                    clear()
                    saldo = input('Digite um valor para Saldo: ')
                    if obrigatorio(saldo) and Pessoa.apenas_numeros(saldo):
                        clear()
                        print(f'Saldo alterado de {cliente.saldo} para {saldo} com sucesso.')
                        time.sleep(2)
                        cliente.saldo = int(saldo)
                        clear()
                elif a == 'LIMITE':
                    clear()
                    limite = input('Digite um valor para Limite: ')
                    if obrigatorio(limite) and Pessoa.apenas_numeros(limite):
                        clear()
                        print(f'Limite alterado de {cliente.limite} para {limite} com sucesso.')
                        time.sleep(2)
                        cliente.limite = int(limite)
                        clear()
                else:
                    clear()
                    print('Comando não reconhecido. Operação cancelada.')
                    time.sleep(2)
                    clear()
        elif a == '5':
            clear()
            print('Logout concluído com sucesso.')
            time.sleep(2)
            clear()
            break

def conta_colaborador_rh(colaborador, bd):
    while True:
        clear()
        a = painel_colaborador_rh(colaborador)
        if a == '1':
            clear()
            print('Área de registro de novo Colaborador ACADY.') 
            print('Abaixo, insira os dados do colaborador: \n')
            while True:
                nome = input('Digite o Nome: ').title()
                if Pessoa.apenas_letras(nome) and obrigatorio(nome):
                    break
            while True:
                sobrenome = input('Digite o Sobrenome: ').title()
                if Pessoa.apenas_letras(sobrenome) and obrigatorio(sobrenome):
                    break
            while True:
                cpf = input('Digite o CPF: ')
                d = True
                if obrigatorio(cpf):
                    for i in bd.values():
                        if cpf == i.cpf:
                            clear()
                            print('Este CPF já foi cadastrado.')
                            time.sleep(2)
                            clear()
                            d = False
                            break
                    if d and Pessoa.apenas_numeros(cpf):
                        break
            while True:
                idade = input('Digite a Idade: ')
                if obrigatorio(idade) and Pessoa.apenas_numeros(idade):
                    break
            while True:
                sexo = input('Digite o Sexo: ').upper()
                if sexo == 'M' or sexo == 'F':
                    break
                clear()
                print("Digite 'm' ou 'f' para o sexo do cliente.")          
                time.sleep(2)
                clear()
            while True:
                clear()
                endereco = input('Digite a Cidade: ').title()
                if obrigatorio(endereco) and Pessoa.apenas_letras(endereco):
                    break
            while True:
                telefone = input('Digite o Telefone: ')
                if obrigatorio(telefone) and Pessoa.apenas_numeros(telefone):
                    break
            while True:
                clear()
                login = input('Digite o Login: ')
                if obrigatorio(login) and login in bd.keys():
                    clear()
                    print('Este login já foi cadastrado.')
                    time.sleep(2)
                    clear()
                if login:
                    break
                else:
                    clear()
                    print('Campo obrigatório.')
                    time.sleep(2)
                    clear()
            while True:
                clear()
                senha = input('Digite a Senha: ')
                if senha:
                    break
                else:
                    clear()
                    print('Campo obrigatório.')
                    time.sleep(2)
                    clear()
            while True:
                clear()
                setor = input('Digite o Setor de atuação (Rh/Caixa): ').title()
                if setor == 'Rh' or setor == 'Caixa':
                    break
                else:
                    clear()
                    print("Digite apenas 'RH' ou 'Caixa'.")
                    time.sleep(2)
                    clear()
            while True:
                clear()
                print('Dados do novo Colaborador ACADY: \n')
                print(f'Nome: {nome}')
                print(f'Sobrenome: {sobrenome}')
                print(f'CPF: {cpf}')
                print(f'Idade: {idade}')
                print(f'Sexo: {sexo}')
                print(f'Endereço: {endereco}')
                print(f'Telefone: +55 035 {telefone}')
                print(f'Login: {login}')
                print(f'Setor: {setor}\n')
                print('Deseja mesmo cadastrar este colaborador (s/n): ')
                a = readchar().upper()
                if a == 'S':
                    try:
                        bd[login] = Colaborador(nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha, setor)
                    except:
                        clear()
                        print('Não foi possível efetuar o cadastro.')
                        time.sleep(2)
                        break
                    clear()
                    print('O colaborador foi cadastrado com sucesso.')
                    time.sleep(2)
                    break
                elif a == 'N':
                    clear()
                    print('Operação cancelada. Os dados foram apagados com sucesso.')
                    time.sleep(2)
                    break
                else:
                    clear()
                    print('Comando não reconhecido. Os dados foram apagados.')
                    time.sleep(2)
        elif a == '2':
            clear()
            login = input('Digite o Login do colaborador que deseja remover: ')
            if obrigatorio(login) and login in bd.keys():
                colaborador = bd[login]
                a = True
            else:
                clear()
                print('Este login não está cadastrado.')
                a = False
                time.sleep(2)
            if a:
                clear()
                print('Dados do Colaborador ACADY: \n')
                print(f'Nome: {colaborador.nome}')
                print(f'Sobrenome: {colaborador.sobrenome}')
                print(f'CPF: {colaborador.cpf}')
                print(f'Idade: {colaborador.idade}')
                print(f'Sexo: {colaborador.sexo}')
                print(f'Endereço: {colaborador.endereco}')
                print(f'Telefone: {colaborador.telefone}')
                print(f'Login: {colaborador.login}')
                print(f'Senha: ************\n')
                print('Deseja mesmo remover este colaborador (s/n): ')
                a = readchar().upper()
                if a == 'S':
                    bd.pop(login)
                    clear()
                    print('A conta foi apagada com sucesso.')
                    time.sleep(2)
                    clear()
                elif a == 'N':
                    clear()
                    print('Operação cancelada.')
                    time.sleep(2)
                    clear()
                else:
                    clear()
                    print('Comando não reconhecido. A conta não foi removida.')
                    time.sleep(2)
        elif a == '3':
            clear()
            login = input('Digite o Login do Colaborador que deseja consultar: ')
            clear()
            if obrigatorio(login) and login in bd.keys():
                colaborador = bd[login]
                a = True
            else:
                clear()
                print('Este login não está cadastrado.')
                a = False
                time.sleep(2)
            if a:
                print('Dados do Colaborador ACADY consultado: \n')
                print(f'Nome: {colaborador.nome}')
                print(f'Sobrenome: {colaborador.sobrenome}')
                print(f'CPF: {colaborador.cpf}')
                print(f'Idade: {colaborador.idade}')
                print(f'Sexo: {colaborador.sexo}')
                print(f'Endereço: {colaborador.endereco}')
                print(f'Telefone: {colaborador.telefone}')
                print(f'Login: {colaborador.login}')
                print(f'Senha: ************')
                print(f'Setor: {colaborador.setor}\n')
                input('Pressione Enter para sair. ')
        elif a == '4':
            clear()
            login = input('Digite o Login do colaborador que deseja alterar: ')
            clear()
            if obrigatorio(login) and login in bd.keys():
                colaborador = bd[login]
                b = True
            else:
                clear()
                print('Este login não está cadastrado.')
                b = False
                time.sleep(2)
                clear()
            if b:
                print('Dados do Colaborador ACADY: \n')
                print(f'Nome: {colaborador.nome}')
                print(f'Sobrenome: {colaborador.sobrenome}')
                print(f'CPF: {colaborador.cpf}')
                print(f'Idade: {colaborador.idade}')
                print(f'Sexo: {colaborador.sexo}')
                print(f'Endereço: {colaborador.endereco}')
                print(f'Telefone: {colaborador.telefone}')
                print(f'Login: {colaborador.login}')
                print(f'Senha: ************')
                print(f'Setor: {colaborador.setor}\n')
                a = input('Digite o dado que deseja alterar: ').upper()
                if a == 'NOME':
                    clear()
                    nome = input('Digite um Nome: ').title()
                    if Pessoa.apenas_letras(nome):
                        clear()
                        print(f'Nome alterado de {colaborador.nome} para {nome} com sucesso.')
                        time.sleep(2)
                        colaborador.nome = nome
                        clear()
                elif a == 'SOBRENOME':
                    clear()
                    sobrenome = input('Digite um Sobrenome: ').title()
                    if Pessoa.apenas_letras(sobrenome):
                        clear()
                        print(f'Sobrenome alterado de {colaborador.sobrenome} para {sobrenome} com sucesso.')
                        time.sleep(2)
                        colaborador.sobrenome = sobrenome
                        clear()
                elif a == 'CPF':
                    clear()
                    cpf = input('Digite um CPF: ')
                    if obrigatorio(cpf) and Pessoa.apenas_numeros(cpf):
                        clear()
                        print(f'CPF alterado de {colaborador.cpf} para {cpf} com sucesso.')
                        time.sleep(2)
                        colaborador.cpf = cpf
                        clear()
                elif a == 'IDADE':
                    clear()
                    idade = input('Digite uma Idade: ')
                    if obrigatorio(idade) and Pessoa.apenas_numeros(idade):
                        clear()
                        print(f'Idade alterada de {colaborador.idade} para {idade} com sucesso.')
                        time.sleep(2)
                        colaborador.idade = idade
                        clear()
                elif a == 'SEXO':
                    clear()
                    sexo = input('Digite um Sexo: ').upper()
                    if sexo == 'F' or sexo == 'M':
                        clear()
                        print(f'Sexo alterado de {colaborador.sexo} para {sexo} com sucesso.')
                        time.sleep(2)
                        colaborador.sexo = sexo
                        clear()
                    else:
                        clear()
                        print('Sexo não reconhecido. Operação cancelada.')
                        time.sleep(2)
                        clear()
                elif a == 'ENDEREÇO':
                    clear()
                    endereco = input('Digite um Endereço: ').title()
                    if obrigatorio(endereco) and Pessoa.apenas_letras(endereco):
                        clear()
                        print(f'Endereço alterado de {colaborador.endereco} para {endereco} com sucesso.')
                        time.sleep(2)
                        colaborador.endereco = endereco
                        clear()
                elif a == 'TELEFONE':
                    clear()
                    telefone = input('Digite um Telefone: ').title()
                    if obrigatorio(telefone) and Pessoa.apenas_numeros(telefone):
                        clear()
                        print(f'Telefone alterado de {colaborador.telefone} para +55 035 {telefone} com sucesso.')
                        time.sleep(2)
                        colaborador.telefone = telefone
                        clear()
                elif a == 'LOGIN':
                    clear()
                    login = input('Digite um Login: ')
                    if obrigatorio(login):
                        clear()
                        print(f'Login alterado de {colaborador.login} para {login} com sucesso.')
                        bd.pop(colaborador.login)
                        bd[login] = colaborador
                        time.sleep(2)
                        colaborador.login = login
                        clear()                  
                elif a == 'SENHA':
                    clear()
                    senha = input('Digite uma Senha: ')
                    clear()
                    print(f'Senha alterada com sucesso.')
                    time.sleep(2)
                    colaborador.senha = senha
                    clear()
                elif a == 'SETOR':
                    clear()
                    setor = input('Digite um Setor (Rh/Caixa): ').title()
                    if setor == 'Rh' or setor == 'Caixa':
                        clear()
                        print(f'Setor alterado de {colaborador.setor} para {setor} com sucesso.')
                        time.sleep(2)
                        colaborador.setor = setor
                        clear()
                else:
                    clear()
                    print('Comando não reconhecido. Operação cancelada.')
                    time.sleep(2)
                    clear()
        elif a == '5':
            clear()
            print('Logout concluído com sucesso.')
            time.sleep(2)
            break
        else:
            clear()
            print('Comando não reconhecido. Operação cancelada.')
            time.sleep(2)
            clear()

def conta_cliente(cliente):
    while True:
        clear()
        a = painel_cliente(cliente)
        if a == '1':
            clear()
            try:
                valor = int(input('Digite o valor que deseja depositar: '))
                cliente.depositar(valor)
            except:
                clear()
                print('Operação cancelada. Digite apenas números, por favor.')
                time.sleep(2)
        elif a == '2':
            clear()
            try:
                valor = int(input('Digite o valor que deseja sacar: '))
                cliente.sacar(valor)
            except:
                clear()
                print('Operação cancelada. Digite apenas números, por favor.')
                time.sleep(2)          
        elif a == '3':
            clear()
            destino = input('Digite o login do destinatário: ')
            if destino in bd.keys():
                destino = bd[destino]
                try:
                    valor = int(input('Digite o valor que deseja transferir: '))
                    cliente.transferir(valor, destino)
                except:
                    clear()
                    print('Operação cancelada. Digite apenas números, por favor.')
                    time.sleep(2)
            else:
                clear()
                print('Este login não está cadastrado.')
                time.sleep(2)
        elif a == '4':
            clear()
            cliente.atividades
            print(f'\nSALDO: {cliente.saldo}\nRENDA MENSAL: {cliente.renda}\nLIMITE: {cliente.limite}')
            input('\nPressione Enter para sair.')
        elif a == '5':
            clear()
            print(f'Informações básicas: \n')
            print(f'Nome: {cliente.nome}')
            print(f'Sobrenome: {cliente.sobrenome}')
            print(f'CPF: {cliente.cpf}')
            print(f'Idade: {cliente.idade}')
            print(f'Sexo: {cliente.sexo}')
            print(f'Endereço: {cliente.endereco}')
            print(f'Telefone: {cliente.telefone}')
            print(f'Login: {cliente.login}')
            print(f'Senha: ************')
            print(f'Conta: {cliente.conta}')
            print(f'Renda: {cliente.renda}')
            print(f'Limite: {cliente.limite}')
            input('\nDigite Enter para sair: ')
        elif a == '6':
            clear()
            print('Logout concluído com sucesso.')
            time.sleep(2)
            break

class Pessoa:
    '''Classe responsável por qualquer instância relacionada à uma pessoa física, seja cliente ou funcionário.'''

    def __init__(self, nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__idade = idade
        self.__sexo = sexo
        self.__endereco = endereco
        self.__telefone = f'+55 035 {telefone}'
        self.__login = login
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def apenas_letras(arg0): 
        '''Verifica se há apenas letras no argumento 1 para ser alterado.'''
        for i in range(10):
            if str(i) in arg0:
                clear()
                print(f'Digite apenas letras.')
                time.sleep(2)
                clear()
                return False
        clear()
        return True

    def apenas_numeros(arg0): 
        '''Verifica se há apenas números no argumento 1 para ser alterado.'''
        try:
            int(arg0)
            clear()
            return True
        except:
            clear()
            print('Digite apenas número.')
            time.sleep(2)
            clear()
            return False

    # declarando as propriedades da classe Pessoa

    @property
    def nome(self):
        return f'{self.__nome}'

    @property
    def sobrenome(self):
        return f'{self.__sobrenome}'

    @property
    def cpf(self):
        return f'{self.__cpf}'

    @property
    def idade(self):
        return f'{self.__idade}'

    @property
    def sexo(self):
        return f'{self.__sexo}'

    @property
    def endereco(self):
        return f'{self.__endereco}'

    @property
    def login(self):
        return f'{self.__login}'

    @property
    def senha(self):
        return f'{self.__senha}'

    @property
    def telefone(self):
        return f'{self.__telefone}'

    # declarando os sets da classe Pessoa
    @nome.setter
    def nome(self, nome):
        if Pessoa.apenas_letras(nome):
            self.__nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        if Pessoa.apenas_letras(sobrenome):
            self.__sobrenome = sobrenome
        
    @cpf.setter
    def cpf(self, cpf):
        if Pessoa.apenas_numeros(cpf):
            self.__cpf = cpf

    @idade.setter
    def idade(self, idade):
        if Pessoa.apenas_numeros(idade):
            self.__idade = idade

    @sexo.setter
    def sexo(self, sexo):
        if Pessoa.apenas_letras(sexo):
            self.__sexo = sexo

    @endereco.setter
    def endereco(self, endereco):
        if Pessoa.apenas_letras(endereco):
            self.__endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        if Pessoa.apenas_numeros(telefone):
            self.__telefone = f'+55 035 {telefone}'

    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self, senha):
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
class Cliente(Pessoa):
 
    __conta = 11989
 
    def __init__(self, nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha, renda, limite, saldo):
        super().__init__(nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha)
        self.__conta = Cliente.__conta + 13  
        self.__renda = renda
        self.__limite = limite
        self.__saldo = saldo
        self.__atividades = []
        Cliente.__conta = self.__conta # atualiza o valor do número conta da sub-classe Cliente

    @property
    def conta(self):
        return f'2276-4 {self.__conta}-5'

    @property
    def renda(self):
        return f'{self.__renda}'

    @property
    def limite(self):
        return f'{self.__limite}'

    @property
    def atividades(self):
        agora = datetime.now() # definindo a variável atual para obter tempo atual
        print(f'Extrato Bancário {agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\n')
        k = 1
        for i in self.__atividades: 
            print(f'{k} - {i[0]} {i[1]} {i[2]} {i[3]}\n')
            k += 1
  
    @property
    def saldo(self):
        return f'{self.__saldo}'   

    @limite.setter
    def limite(self, limite):
        if Pessoa.apenas_numeros(limite):
            self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        if Pessoa.apenas_numeros(saldo):
            self.__saldo = saldo

    @renda.setter
    def renda(self, renda):
        if Pessoa.apenas_numeros(renda):
            self.__renda = renda

    def depositar(self, valor):
        if valor < 0:
            clear()
            print('Apenas valores positivos para depósito. Obrigado.')
            time.sleep(2)
            return
        clear()
        print(f'DEPOSITAR\nNome: {self.nome} {self.sobrenome}\nConta: {self.conta}')
        agora = datetime.now() # definindo a variável atual para obter tempo atual
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\nR${valor}\n')
        print("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        a = readchar().upper()
        if a == 'S':
            self.__saldo += valor
            agora = datetime.now() # definindo a variável atual para obter tempo atual
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}', 'Depósito', f'R${valor}',  ''])
            clear()
            print('Insira o dinheiro no compartimento abaixo.')
            time.sleep(2)
        elif a == 'N':
            clear()
            print('Operação cancelada.')
            time.sleep(2)
        else:
            clear()
            print('Comando não identificado. Operação cancelada.')
            time.sleep(2)

    def sacar(self, valor):
        if valor < 0:
            clear()
            print('Apenas valores positivos para saque. Obrigado.')
            time.sleep(2)
            return
        if self.__saldo < valor:
            clear()
            print('Não há saldo suficiente para esta ação. Obrigado.')
            time.sleep(2)
            return
        clear()
        print(f'SACAR\nNome: {self.nome} {self.sobrenome}\nConta: {self.conta}')
        agora = datetime.now() # definindo a variável atual para obter tempo atual
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\nR${valor}\n')
        print("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        a = readchar().upper()
        if a == 'S':
            agora = datetime.now() # definindo a variável atual para obter tempo atual
            self.__saldo -= valor
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}','Saque', f'R${valor}',  ''])
            clear()
            print('Retire seu dinheiro.')
            time.sleep(2)
        elif a == 'N':
            clear()
            print('Operação cancelada.')
            time.sleep(2)
        else:
            clear()
            print('Comando não identificado. Operação cancelada.')
            time.sleep(2)

    def transferir(self, valor, destino):
        if valor < 0:
            clear()
            print('Apenas valores positivos para transferência. Obrigado.')
            time.sleep(2)
            return
        if self.__saldo < valor:
            clear()
            print('Não há saldo suficiente para esta ação. Obrigado.')
            time.sleep(2)
            return
        clear()
        print(f'TRANSFERIR\nDe: {self.nome} {self.sobrenome} \nConta: {self.conta}\nCPF originário: {self.cpf}\n\nR${valor}\n')
        print(f'Para: {destino.nome} {destino.sobrenome} \nConta: {destino.conta}\nCPF destinatário: {destino.cpf}\n')
        agora = datetime.now() # definindo a variável atual para obter tempo atual
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\n')
        print("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        a = readchar().upper()
        if a == 'S':
            agora = datetime.now() # definindo a variável atual para obter tempo atual
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}', 'Transferência', f'{destino.nome} {destino.sobrenome}', f'R${valor}'])
            self.__saldo -= valor
            destino.__saldo += valor
            clear()
            print('Transferência executada com sucesso.')
            time.sleep(2)
        elif a == 'N':
            clear()
            print('Operação cancelada.')
            time.sleep(2)
        else:
            clear()
            print('Comando não identificado. Operação cancelada.')
            time.sleep(2)             

class Colaborador(Pessoa):

    __matricula = 990

    def __init__(self, nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha, setor):
        super().__init__(nome, sobrenome, cpf, idade, sexo, endereco, telefone, login, senha)
        self.__matricula = Colaborador.__matricula + 10
        self.__setor = setor.title()
        Colaborador.__matricula = self.__matricula # atualiza o valor do número conta da sub-classe Cliente

    @property
    def matricula(self):
        return f'{self.__matricula}'

    @property
    def setor(self):
        return f'{self.__setor}'

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

clear = lambda: os.system('clear') # criando função lambda para simplificação de uso
init(autoreset=True) # iniciando o init do colorama
agora = datetime.now() # definindo a variável atual para obter tempo atual
bd = {} # banco de dados de clientes
admin = Colaborador('Admin', '', '', '', '', '', '', 'admin', 'admin', 'Rh') # definindo um rh padrão para cadastramento de outros colaboradores
bd['admin'] = admin

'''
O CÓDIGO DENTRO DESSE COMENTÁRIO DEVE SER USADO APENAS PARA TESTE RÁPIDO DO SISTEMA

admin2 = Colaborador('Admin', '', '', '', '', '', '', 'admin2', 'admin2', 'Caixa') # definindo um rh padrão para cadastramento de outros colaboradores
usuario = Cliente('Nome', 'Sobrenome', '123456789', '21', 'M', 'Cidade', '991123789', 'login', 'senha', 1000, 1000 ,1000) # definindo um rh padrão para cadastramento de outros colaboradores
bd['admin2'] = admin2
bd['usuario'] = usuario
'''

while True:
    clear()
    a = painel_apresentacao()
    if a == '1':
        login = input('Digite seu login: ')
        if login in bd.keys():
            cliente = bd[login]  
            senha = input('Digite sua senha: ')
            if cliente.checa_senha(senha):
                if type(cliente) == Colaborador:
                    if cliente.setor == 'Caixa':
                        conta_colaborador_cx(cliente, bd)
                    elif cliente.setor == 'Rh':
                        conta_colaborador_rh(cliente, bd)
                else:
                    conta_cliente(cliente)
            else:
                print('\nSenha incorreta.')
                time.sleep(2)
        else:
            print('Este login não está cadastrado.')
            time.sleep(2)
    elif a == '2':
        clear()
        break
