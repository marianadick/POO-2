'''Exercício 6: Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno, imprima o número de alunos com média
maior ou igual a 7.0.'''

count = 0
notas = []

for _ in range(10):
    media = 0
    for _ in range(4):
        nota = float(input('Digite uma nota:'))
        media += nota
    media = media/4
    notas.append(media)
    if (media >= 7.0):
        count += 1

print(f'Vetor com as notas dos alunos: {notas}')
print(f'Num de alunos que possuem média >= 7.0: {count}')
