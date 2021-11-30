from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura 

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento
        
    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @abstractmethod
    def apresentar(self):
        pass

class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int, autonomia: int, envergadura: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self):
        return self.__autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self.__autonomia = autonomia

    @property
    def envergadura(self):
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, envergadura):
        self.__envergadura = envergadura

    def apresentar(self):
        print(f'Tipo do Veiculo: Aereo, nome: {self.nome}')
        print(f'altura: {self.altura} m, comprimento: {self.comprimento} m, carga: {self.carga} t')
        print(f'velocidade: {self.velocidade} km/h, autonomia: {self.autonomia} km, envergadura: {self.envergadura} m')

class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int, rodas: str, motor: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__rodas = rodas
        self.__motor = motor

    @property
    def rodas(self):
        return self.__rodas
    
    @rodas.setter
    def rodas(self, rodas):
        self.__rodas = rodas

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def apresentar(self):
        print(f'Tipo do Veiculo: Terrestre, nome: {self.nome}')
        print(f'altura: {self.altura} m, comprimento: {self.comprimento} m, carga: {self.carga} t')
        print(f'velocidade: {self.velocidade} km/h, motor: {self.motor}, rodas: {self.rodas}')

class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: int, comprimento: int, carga: int, velocidade: int, boca: int, calado: int):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self):
        return self.__boca

    @boca.setter
    def boca(self, boca):
        self.__boca = boca

    @property
    def calado(self):
        return self.__calado

    @calado.setter
    def calado(self, calado):
        self.__calado = calado     

    def apresentar(self):
        print(f'Tipo do Veiculo: Aquatico, nome: {self.nome}')
        print(f'altura: {self.altura} m, comprimento: {self.comprimento} m, carga: {self.carga} t')
        print(f'velocidade: {self.velocidade} km/h, boca: {self.boca} m, calado: {self.calado} m')   

class Catálogo():
    def __init__(self, nome, ano, veiculoscadastrados):
        self.__nome = nome
        self.__ano = ano
        self.__veiculoscadastrados = veiculoscadastrados
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano 

    @property
    def veiculoscadastrados(self):
        return self.__veiculoscadastrados

    def adicionar_veiculo(self, veiculo: Transporte):
        if isinstance(veiculo, Transporte):
            self.veiculoscadastrados.append(veiculo)

    def mostrar_veiculos(self):
        for veiculo in self.veiculoscadastrados:
            veiculo.apresentar()
            print()

def main():
    TransporteAereo1 = TransporteAereo('aviao', 2, 2, 2, 2, 2, 2)
    TransporteTerrestre1 = TransporteTerrestre('golzinho', 2, 2, 2, 2, 'muito boas', 'potente')
    TransporteAquatico1 = TransporteAquatico('peixe', 1, 2, 3, 4, 1, 2)
    
    Catalogo1 = Catálogo('Testezinho', 2004, [TransporteAereo1, TransporteAquatico1])
    Catalogo1.adicionar_veiculo(TransporteTerrestre1)
    Catalogo1.mostrar_veiculos()

main()