class main:
    pass 

print('Testando Projeto')

from cliente import cliente
from conta import conta

c1 = cliente('Marina', '996733623')
conta = conta(c1.get_nome(), 6565, 0)
conta.deposita(100)
conta.saque(50)
conta.extrato()
print(conta._titular, 'Número: ', conta._numero, 'Seu saldo: ', conta._saldo)
