from abc import abstractmethod

class Conta:
    def __init__(self, agencia: int, conta: int, saldo: int):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    # método abstrato para fazer ocm que cada classe crie com sua própira funcionalidade
    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    # adiciona o valor de limite extra de saque
    def __init__(self, agencia, conta, saldo, limite: int = 100):
        Conta.__init__(self,agencia, conta, saldo)
        self._limite = limite

    # para obter o valor de limite dentro da classe
    @property
    def limite(self):
        return self._limite

    # função para efetuar o saque da conta
    def sacar(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
        else:
            print('saldo insuficiente para saque')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('saldo insuficiente para o saque')