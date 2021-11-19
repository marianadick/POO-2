'''Crie um sistema que gerencia o cadastro de alunos e professores em turmas. Os usuários
serão os membros da secretaria. Eles devem conseguir visualizar os alunos matriculados em
cada turma, com seus dados, suas notas e presenças. Além disso, os secretários precisam ter
acesso a dados cadastrais dos professores associados à disciplina.'''

class Aluno():
    def __init__(self, nome: str, turmas=[], notas={}, presencas={}):
        self.__nome = nome
        self.__turmas = turmas
        self.__notas = notas
        self.__presencas = presencas

    @property
    def nome(self):
        return self.__nome

    @property
    def turmas(self):
        return self.__turmas

    @property
    def notas(self):
        return self.__notas

    @property
    def presencas(self):
        return self.__presencas

    def realizar_matricula(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)
            self.notas[turma.materia]= []
            self.presencas[turma.materia]= []
        else:
            return 'Aluno já está cadastrado'

    def computar_nota(self, turma, nota: int):
        if turma in self.turmas:
            self.notas[turma.materia].append(nota)
        else:
            return 'Aluno não está cadastrado na turma'

    def computar_presenca(self, turma, presenca):
        if turma in self.turmas:
            self.presencas[turma.materia].append(presenca)
        else:
            return 'Aluno não está cadastrado na turma'

class Professor():
    def __init__(self, nome: str, disciplinas = []):
        self.__nome = nome
        self.__disciplinas = disciplinas

    @property
    def nome(self):
        return self.__nome

    @property
    def disciplinas(self):
        return self.__disciplinas

    def adicionar_disciplina(self, turma):
        self.disciplinas.append(turma.materia)

class Turma():
    def __init__(self, materia):
        self.__materia = materia

    @property
    def materia(self):
        return self.__materia

class Secretaria():
    def __init__(self, alunos=[], professores=[]):
        self.__alunos = alunos
        self.__professores = professores

    @property
    def alunos(self):
        return self.__alunos

    @property
    def professores(self):
        return self.__professores

    def mostrar_alunos(self):
        print('Relatório de alunos:')
        for aluno in self.alunos:
            print(f'Aluno(a) {aluno.nome}')
            print(f'Notas = {aluno.notas}')
            print(f'Presenças = {aluno.presencas}')
            print()


    def mostrar_professores(self):
        print('Relatório de professores:')
        s = ', '
        for professor in self.professores:
            print(f'Prof. {professor.nome}')
            print(f'Disciplinas = {s.join(professor.disciplinas)}')
            print()

def main():
    Turma1 = Turma('Programação Orientada a Objetos')
    Turma2 = Turma('Introdução à Computação')

    Aluno1 = Aluno('Mariana S Dick')
    Aluno1.realizar_matricula(Turma1)
    Aluno1.computar_nota(Turma1, 10)
    Aluno1.computar_nota(Turma1, 6)
    Aluno1.computar_presenca(Turma1, 'V')
    Aluno1.computar_presenca(Turma1, 'F')

    Professor1 = Professor('Jonata')
    Professor1.adicionar_disciplina(Turma1)
    Professor1.adicionar_disciplina(Turma2)
 
    Secretaria1 = Secretaria([Aluno1], [Professor1])
    Secretaria1.mostrar_alunos()
    Secretaria1.mostrar_professores()

main()
    
