from conta import Conta, ContaCorrente, ContaPoupanca

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self,nome, idade)
        self._conta = None

    # para acessar a conta
    @property
    def conta(self):
        return self._conta

    # para setar o valor de conta
    @conta.setter
    def conta(self, conta):
        self._conta = conta

    # adiciona uma conta ao cliente
    def adicionar_conta(self, conta):
        self.conta = conta
