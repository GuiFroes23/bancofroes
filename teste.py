from models.cliente import Cliente
from models.conta import Conta

guilherme: Cliente = Cliente("Guilherme", "guilhermefroes-@hotmail.com", "131.471.099-09", "12/07/2002")
cecilia: Cliente= Cliente("Cecilia", "Ceciliafroes-@hotmail.com", "516.576.279-34", "22/11/1960")

print(guilherme)
print(cecilia)

conta1: Conta = Conta(guilherme)
conta2: Conta = Conta(cecilia)

print(conta1)
print(conta2)