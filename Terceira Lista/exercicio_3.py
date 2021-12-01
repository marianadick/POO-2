'''Exercicio 3: Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve
terminar quando for lida uma string vazia como nome. Escreva uma função que retorna
a média do aluno, dado seu nome.'''

notas = {}

def cadastro_de_notas():
    while True: 
        nome = input('Insira o nome do aluno: ')
        if (nome == ''):
            break

        if nome not in notas.keys():
            nota1 = int(input(f'Insira a primeira nota de {nome}: '))
            nota2 = int(input(f'Insira a segunda nota de {nome}: '))
            notas[nome] = [nota1, nota2]
        else:
            print('As notas já foram cadastradas')

def retorna_media(nome):
    if nome in notas:
        media = (notas[nome][0] + notas[nome][1])/2
        return f'A média de {nome} é {media}!'
    else:
        return 'As notas não foram cadastradas'      

def main():
    cadastro_de_notas()
    print(retorna_media('Mariana'))

main()



    

