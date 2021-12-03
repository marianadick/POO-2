class Produto():
    def __init__(self, codigo, descricao, categoria,
                 quantidade=0, preco_unitario=0, cliente=None):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario
        self.__cliente = cliente

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        return self.__descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
        return self.__categoria

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        return self.__quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
        return self.__preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
        return self.__cliente

    def preco_total(self):
        preco_total = self.preco_unitario * self.quantidade
        return preco_total
