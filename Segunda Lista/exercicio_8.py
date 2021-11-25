'''Exercício 8: Faça um Programa que peça a idade e a altura de 5 pessoas, armazene
cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa
a ordem lida.'''

idades = []
alturas = []

for _ in range(5):
    altura = float(input('Qual sua altura? '))
    alturas.append(altura)
    idade = int(input('Qual sua idade? '))
    idades.append(idade)

idades.reverse()
alturas.reverse()

print(f'Idades: {idades}')
print(f'Alturas: {alturas}')
