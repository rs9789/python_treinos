"""
Código sujeito a mais modificações futuras
"""

from conta import ContaPoupanca, ContaCorrente
from pessoas import Cliente

# realizando todos os testes das classes
c1 = ContaCorrente(1234567,11111111,0)
c2 = ContaPoupanca(111111,22222, 0)

cliente1 = Cliente('Rodrigo', 33)

cliente1.adicionar_conta(c2)

cliente1.conta.deposito(20)
cliente1.conta.sacar(20)
