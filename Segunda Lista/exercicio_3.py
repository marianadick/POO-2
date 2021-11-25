'''Exercício 3:  Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

notas = []
media = 0

for _ in range(4):
    nota = int(input('Digite uma nota: '))
    notas.append(str(nota))
    media += nota

media = media/4

print('Notas: ', ', '.join(notas))
print(f'Média: {media:.2f}')