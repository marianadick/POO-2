'''Crie as classes necessárias para um sistema de gerenciamento de uma biblioteca. Os
bibliotecários deverão preencher o sistema com o título do livro, os autores, o ano, a editora, a
edição e o volume. A biblioteca também terá um sistema de pesquisa (outro software), portanto
será necessário conseguir acessar os atributos típicos de pesquisa (nome, autor, …).'''

class Livro():
    def __init__(self, titulo: str, autores: str, ano: str, editora: str, edicao=1, volume=1):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora
        self.__edicao = edicao
        self.__volume = volume

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autores(self):
        return self.__autores

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def edicao(self):
        return self.__edicao          

    @property
    def volume(self):
        return self.__volume              

class Biblioteca():
    def __init__(self, livros: list):
        self.__livros = livros

    @property
    def livros(self):
        return self.__livros

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def exibir_livros(self):
        c = 0
        for livro in self.livros:
            c += 1
            print(f'{c}. {livro.titulo} ({livro.ano}), por {livro.autores}, editora {livro.editora}, ed. {livro.edicao}, vol. {livro.volume}')

def main():
    livro1 = Livro('Admirável mundo novo', 'Aldous Huxley', '1932', 'Biblioteca Azul')
    livro2 = Livro('Morte na Mesopotâmia', 'Agatha Christie', '1936', 'Arqueiro', '19')
    livro3 = Livro('Life, the Universe and Everything', 'Douglas Adams', '1982', 'Del Rey', '1', '3')
    livro4 = Livro('Cidades de Papel', 'John Green', '2008', 'Intrinseca')

    Biblioteca1 = Biblioteca([livro1, livro2, livro3])
    Biblioteca1.adicionar_livro(livro4)
    Biblioteca1.exibir_livros()

main()