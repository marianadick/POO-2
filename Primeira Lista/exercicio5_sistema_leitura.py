'''Implemente um sistema de leitura online que possua as seguintes funcionalidades:
● Criação e gerenciamento de usuários 
● Busca pelos livros disponíveis (reutilizar classes do exercício 2)  
● Leitura de livro (página por página)
○ Apenas um usuário por vez
○ Apenas um livro ativo por usuário
A implementação dos métodos referentes a visualização na tela (display) podem ser
substituídos por um comentário dentro do métodos, ex. “”” atualiza elementoX na tela “””'''

class Usuário():
    def __init__(self, nome: str, senha: str):
        self.__nome = nome
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

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

class Sistema():
    def __init__(self, livros: list, usuarios: list, ocupado=False):
        self.__livros = livros
        self.__usuarios = usuarios
        self.__ocupado = ocupado

    @property
    def livros(self):
        return self.__livros

    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def ocupado(self):
        return self.__ocupado

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def exibir_livros(self):
        c = 0
        for livro in self.livros:
            c += 1
            print(f'{c}. {livro.titulo} ({livro.ano}), por {livro.autores}, editora {livro.editora}, ed. {livro.edicao}, vol. {livro.volume}')

    def busca_livro(self):
        pesquisa = input('Digite o título do livro que procura: ')
        livroencontrado = False
        for livro in self.livros:
            if pesquisa == livro.titulo:
                i = self.livros.index(livro)
                print(f'{livro.titulo} ({livro.ano}), por {livro.autores}, editora {livro.editora}, ed. {livro.edicao}, vol. {livro.volume}')
                livroencontrado = True
        if not livroencontrado:
            print('Livro indisponível!')   
        print() 

    def adicionar_usuario(self, usuario: Usuário):
        self.usuarios.append(usuario)

    def leitura_de_livro(self, usuario):
        if self.ocupado:
            print('Sistema ocupado')
        else:
            ocupado = True
            print('Livros disponíveis:')
            self.exibir_livros()
            escolha = int(input('Digite o número do livro escolhido: '))
            '''Abre o livro'''
            while True:
                terminar_sessao = input('Digite ok para terminar sessão: ')
                if terminar_sessao == 'ok':
                    ocupado = False
                    '''fecha o livro'''
                    break
                else:
                    print('Entrada inválida')

def main():
    usuario1 = Usuário('Mariana', '1234')
    usuario2 = Usuário('Mariane', '4321')

    livro1 = Livro('Admirável mundo novo', 'Aldous Huxley', '1932', 'Biblioteca Azul')
    livro2 = Livro('Morte na Mesopotâmia', 'Agatha Christie', '1936', 'Arqueiro', '19')
    livro3 = Livro('Life, the Universe and Everything', 'Douglas Adams', '1982', 'Del Rey', '1', '3')

    Sistema1 = Sistema([livro1, livro2, livro3], [usuario1, usuario2])
    Sistema1.busca_livro()
    Sistema1.leitura_de_livro(usuario1)

main()



            
