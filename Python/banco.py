import os  # import para os.system('clear')
import time  # import para time.sleep()
from passlib.hash import pbkdf2_sha256 as cryp # import para criptografia de senhas

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
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

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
    '''Definição da classe Cliente, sub-classe de da classe Pessoa.'''
 
    __conta = 11989
 
    def __init__(self, nome, sobrenome, cpf, idade, endereco, login, senha, renda, limite, saldo):
        super().__init__(nome, sobrenome, cpf, idade, endereco, login, senha)
        self.__conta = Cliente.__conta + 13  
        self.__renda = renda
        self.__limite = limite
        self.__saldo = saldo    
        Cliente.__conta = self.__conta # atualiza o valor do número conta da sub-classe Cliente

    @property
    def conta(self):
        return f'2276 {self.__conta}-5'

    @property
    def renda(self):
        return f'{self.__renda}'

    @property
    def limite(self):
        return f'{self.__limite}'

    @property
    def saldo(self):
        return f'{self.__saldo}'   
        
    @renda.setter
    def renda(self, renda):
        if Pessoa.apenas_numeros(self.renda, renda):
            self.__renda = renda
    @limite.setter
    def limite(self, limite):
        if Pessoa.apenas_numeros(self.__limite, limite):
            self.__limite = limite

    @saldo.setter
    def saldo(self, saldo):
        if Pessoa.apenas_numeros(self.__saldo, saldo):
            self.__saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            clear()
            print('Apenas valores positivos para depósito. Obrigado.')
            time.sleep(2)
            return
        self.__saldo += valor

    def sacar(self, valor):
        if valor < 0:
            clear()
            print('Apenas valores positivos para saque. Obrigado.')
            time.sleep(2)
            return
        self.__saldo -= valor

    def transferir(self, valor, destino):
        if valor < 0:
            print('Apenas valores positivos para transferência. Obrigado.')
            time.sleep(2)
            return
        self.__saldo -= valor
        destino.__saldo += valor

    

class Funcionario(Pessoa):

    __matricula = 990

    def __init__(self, nome, sobrenome, cpf, idade, endereco, login, senha):
        super().__init__(nome, sobrenome, cpf, idade, endereco, login, senha)
        self.__matricula = Funcionario.__matricula + 10  
        Funcionario.__matricula = self.__matricula # atualiza o valor do número conta da sub-classe Cliente

















clear = lambda: os.system('clear')

douglas = Cliente('douglas', 'oliveira', 987654, 21, 'maria da fé', 'douglasrasr', 'asdd1312d',1500, 5000, 10000)

print(douglas.nome)
print(douglas.sobrenome)
print(douglas.cpf)
print(douglas.idade)
print(douglas.endereco)
print(douglas.login)
print(douglas.senha)
print(douglas.renda)
print(douglas.conta)
print(douglas.limite)
print(douglas.saldo)






