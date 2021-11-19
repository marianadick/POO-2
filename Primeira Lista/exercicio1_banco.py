'''O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de 
seus correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco 
controla apenas o nome e o telefone de cada cliente. A conta corrente apresenta um saldo e 
uma lista de operações de saques e depósitos. Quando o cliente fizer um saque, diminuiremos 
o saldo da conta corrente. Quando ele fizer um depósito, aumentaremos o saldo. O banco 
oferece também contas especiais, com limite especial além do saldo, e conta poupança, que 
oferece um rendimento mensal sempre que o saldo na conta completa um mês. Evidentemente 
é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos e um resumo 
com todas as informações da conta e seus respectivos clientes.'''

class Cliente:
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
        
    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone
        return self.__telefone
    
class Conta():
    def __init__(self, num: int, titular: list, saldo: float, transacoes = []):
        self.__num = num
        self.__titular = titular
        self.__saldo = saldo
        self.__transacoes = [("Saldo: ", self.saldo)]
 
    @property
    def num(self):
        return self.__num
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo
        return self.__saldo
    
    def add_titular(self, cliente: Cliente):
        self.__titular.append(cliente)
        return self.titular
        
    def deposito(self, valor):
        self.__saldo += valor
        self.transacoes.append(('Deposito: + ', valor))
        self.transacoes.append(('Novo saldo: ', self.saldo))
        return self.saldo
        
    def saque(self, valor):
        if self.__saldo >= valor: 
            self.__saldo -= valor
            self.transacoes.append(('Saque: - ', valor))
            self.transacoes.append(('Novo saldo: ', self.saldo))
        return self.saldo
    
    def verificar_saldo(self):
        (f'O seu saldo é de R${self.saldo: .2f}')
        
    def extrato(self):
        print(f'Extrato da Conta de Número {self.num}')
        for i in self.transacoes:
            print(f'{i[0]}R${i[1]: .2f}')
        print()
            
    def resumo(self):
        print(f'Resumo da Conta de Número {self.num}')
        print('Titulares:')
        for titular in self.titular:
            print(f'{titular.nome} - Tel: {titular.telefone}')
        print(f'Saldo: R${self.saldo: .2f}')
        print()

class Especial(Conta):
    def __init__(self, num: int, titular: list, saldo: float, transacoes = [], limite = 1000, divida = 0):
        super().__init__(num, titular, saldo, transacoes)
        self.__limite = limite
        self.__divida = divida
        
    @property
    def limite(self):
        return self.__limite
    
    @property
    def divida(self):
        return self.__divida    

    def usar_limite_especial(self, valor):
        if valor <= self.limite:
            self.saldo += valor
            self.__divida += (valor + 0.01 * valor)
            self.__limite -= valor
            self.transacoes.append(('Solicitação de Limite Especial: + ', valor))
            self.transacoes.append(('Novo saldo: ', self.saldo))
            self.transacoes.append(('Novo limite: ', self.limite))
        
    def devolver_limite_especial(self, valor):
        if valor == self.divida:
            self.__limite += int(valor - 0.01 * valor)
            self.__divida -= valor
            self.saldo -= valor
            self.transacoes.append(('Devolução de Limite Especial: - ', valor))
            self.transacoes.append(('Novo saldo: ', self.saldo))
            self.transacoes.append(('Novo limite: ', self.limite))
        else:
            print(f'O valor a pagar é de {self.divida}')
            print()
        
    def resumo_limite_especial(self):
        print(f'Resumo de Limite Especial da Conta de Número {self.num}')
        print('Taxa do banco: 1%')
        print(f'Valor pendente: {self.divida}')
        print(f'Valor liberado: {self.limite}')
        print()

class Poupanca(Conta):
    def __init__(self, num: int, titular: list, saldo: float, transacoes = []):
        super().__init__(num, titular, saldo, transacoes)
        
    def rendimentos_mensais(self):
        valor = self.saldo*0.01
        self.saldo += valor
        self.transacoes.append(('Rendimentos mensais: + ', valor))
        self.transacoes.append(('Novo saldo: ', self.saldo))
          
def main():
    Cliente1 = Cliente('Fulaninha da Silva', '(48) 9 0000-0000')
    Cliente2 = Cliente('Beltraninho Silva', '(48) 9 00001-0001')
    Cliente3 = Cliente('Beltraninho Silva Junior', '(48) 9 1111-0000')
    
    Conta1 = Conta(123, [Cliente1, Cliente2, Cliente3], 0)
    Conta1.deposito(50)
    Conta1.saque(25)
    Conta1.extrato()
    Conta1.resumo()
    
    Conta2 = Especial(221, [Cliente1, Cliente2, Cliente3], 250)
    Conta2.usar_limite_especial(125)
    Conta2.devolver_limite_especial(126.25)
    Conta2.resumo_limite_especial()
    Conta2.extrato()

    
    Conta3 = Poupanca(155, [Cliente1, Cliente2, Cliente3], 100)
    Conta3.rendimentos_mensais()
    Conta3.extrato()
    
main()