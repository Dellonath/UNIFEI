import os  # import para os.system('clear')
import time  # import para time.sleep()
from passlib.hash import pbkdf2_sha256 as cryp # import para criptografia de senhas
from colorama import Fore, Back, Style, init # import para fontes coloridas
import sys # necessário importar para readchar() 
import tty # necessário importar para readchar() 
import termios # necessário importar para readchar()
from datetime import datetime # usado para datetime.now() para informar a data atual

def readchar(): # esta é a implementação do readchar(), esta função cumpre a função do input() mas sem exigir a tecla Enter
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
    print(Fore.CYAN + 'Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print(Fore.CYAN + '1 - Login.')
    print(Fore.CYAN + '2 - Registrar.\n')
    return readchar()

def painel_cliente(cliente):
    print(Style.BRIGHT + Fore.CYAN + f'Olá, {cliente.nome} {cliente.sobrenome}, bem-vindo à sua ACADY Account.')
    print(Fore.CYAN + 'CLIENTE')
    print(Fore.CYAN + "Lembre-se de utilizar apenas 's' para SIM e 'n' para NÃO.")
    print(Fore.CYAN + 'Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print(Fore.CYAN + '1 - Depositar')
    print(Fore.CYAN + '2 - Sacar')
    print(Fore.CYAN + '3 - Transferir')
    print(Fore.CYAN + '4 - Consultar extrato')
    print(Fore.CYAN + '5 - Sair')
    return readchar()

def painel_colaborador(colaborador):
    print(Style.BRIGHT + Fore.CYAN + f'Olá, {colaborador.nome} {colaborador.sobrenome}, bem-vindo à sua ACADY Account.')
    print(Fore.CYAN + 'COLABORADOR')
    print(Fore.CYAN + "Lembre-se de utilizar apenas 's' para SIM e 'n' para NÃO.")
    print(Fore.CYAN + 'Abaixo há algumas opções, pressione o que você deseja fazer: ')
    print(Fore.CYAN + '1 - Criar cliente')
    print(Fore.CYAN + '2 - Remover cliente ')
    print(Fore.CYAN + '3 - Consultar cliente')
    print(Fore.CYAN + '4 - Alterar cliente')
    print(Fore.CYAN + '5 - Sair ')
    return readchar()

class Pessoa:
    '''Classe responsável por qualquer instância relacionada à uma pessoa física, seja cliente ou funcionário.'''

    def __init__(self, nome, sobrenome, cpf, idade, endereco, login, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__idade = idade
        self.__endereco = endereco
        self.__login = login
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def apenas_letras(arg0, arg1): 
        '''Verifica se há apenas letras no argumento 1 para ser alterado.'''
        for i in range(10):
            if str(i) in arg1:
                clear()
                print(f'Digite apenas letras. Por favor.')
                time.sleep(2)
                return False
        clear()
        print(f'O dado foi alterado de {arg0} para {arg1} com sucesso.')
        time.sleep(2)
        return True

    def apenas_numeros(arg0, arg1): 
        '''Verifica se há apenas números no argumento 1 para ser alterado.'''
        try:
            int(arg1)
            clear()
            print(f'O dado foi alterado de {arg0} para {arg1} com sucesso.')
            time.sleep(2)
            return True
        except:
            clear()
            print('Digite apenas número. Por favor.')
            time.sleep(2)
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
    def endereco(self):
        return f'{self.__endereco}'

    @property
    def login(self):
        return f'{self.__login}'

    @property
    def senha(self):
        return f'{self.__senha}'

    # declarando os sets da classe Pessoa
    @nome.setter
    def nome(self, nome):
        if Pessoa.apenas_letras(self.nome, nome):
            self.__nome = nome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        if Pessoa.apenas_letras(self.sobrenome, sobrenome):
            self.__sobrenome = sobrenome
        
    @cpf.setter
    def cpf(self, cpf):
        if Pessoa.apenas_numeros(self.cpf, cpf):
            self.__cpf = cpf

    @idade.setter
    def idade(self, idade):
        if Pessoa.apenas_numeros(self.idade, idade):
            self.__idade = idade

    @endereco.setter
    def endereco(self, endereco):
        if Pessoa.apenas_letras(self.endereco, endereco):
            self.__endereco = endereco

    @login.setter
    def login(self, login):
        self.__login = login

    @senha.setter
    def senha(self):
        return f'{self.__senha}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
class Cliente(Pessoa):
 
    __conta = 11989
 
    def __init__(self, nome, sobrenome, cpf, idade, endereco, login, senha, renda, limite, saldo):
        super().__init__(nome, sobrenome, cpf, idade, endereco, login, senha)
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
        clear()
        print(f'Extrato Bancário {agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\n')
        k = 1
        for i in self.__atividades: 
            print(f'{k} - {i[0]} {i[1]} {i[2]} {i[3]}\n')
            k += 1
  
    @property
    def saldo(self):
        return f'{self.__saldo}'   

    @limite.setter
    def limite(self, limite, destino):
        if Pessoa.apenas_numeros(self.__limite, limite):
            self.__limite = limite

    def depositar(self, valor):
        if valor < 0:
            clear()
            print('Apenas valores positivos para depósito. Obrigado.')
            time.sleep(2)
            return
        clear()
        print(f'DEPOSITAR\nNome: {self.nome} {self.sobrenome}\nConta: {self.conta}')
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\nR${valor}\n')
        a = input("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        if a == 's':
            self.__saldo += valor
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}', 'Depósito', f'R${valor}',  None])
            clear()
            print('Insira o dinheiro no compartimento abaixo.')
            time.sleep(2)
        elif a == 'n':
            clear()
            print('Operação cancelada.')
            time.sleep(2)
        else:
            clear()
            print('Comando não identificado. Operação cancelada.')
            time.sleep(2)
        self.__saldo += valor

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
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\nR${valor}\n')
        a = input("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        if a == 's':
            self.__saldo -= valor
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}','Saque', f'R${valor}',  None])
            clear()
            print('Retire seu dinheiro.')
            time.sleep(2)
        elif a == 'n':
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
        print(f'TRANSFERIR\nDe: {self.nome} {self.sobrenome} \nConta: {self.conta}\nCPF originário: {self.cpf}')
        print(f'Para: {destino.nome} {destino.sobrenome} \nConta: {destino.conta}\nCPF destinatário: {destino.cpf}')
        print(f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}\nR${valor}\n')
        a = input("Pressione 's' para confirmar a ação ou 'n' para cancelar: ")
        if a == 's':
            self.__atividades.append([f'{agora.day}/{agora.month}/{agora.year} {agora.hour}:{agora.minute}:{agora.second}', 'Transferência', f'R${valor}', f'{destino.nome} {destino.sobrenome}', ])
            self.__saldo -= valor
            destino.__saldo += valor
            clear()
            print('Transferência executada com sucesso.')
            time.sleep(2)
        elif a == 'n':
            clear()
            print('Operação cancelada.')
            time.sleep(2)
        else:
            clear()
            print('Comando não identificado. Operação cancelada.')
            time.sleep(2)             

class colaborador(Pessoa):

    __matricula = 990

    def __init__(self, nome, sobrenome, cpf, idade, endereco, login, senha, setor):
        super().__init__(nome, sobrenome, cpf, idade, endereco, login, senha)
        self.__matricula = colaborador.__matricula + 10
        self.__setor = setor
        colaborador.__matricula = self.__matricula # atualiza o valor do número conta da sub-classe Cliente

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

douglas = Cliente('NOME', 'SOBRENOME', 123456789, 25, 'ENDERECO', 'LOGIN', 'SENHA', 1000, 1000, 1000)
mario = Cliente('NOME2', 'SOBRENOME2', 987654321, 23, 'ENDERECO2', 'LOGIN2', 'SENHA2', 2000, 2000, 2000)


douglas.sacar(400)
douglas.depositar(300)
douglas.transferir(300, mario)
douglas.atividades








