'''Exercício 2:  Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.'''

vetor = [float(x) for x in input().split()]
vetor.reverse()

for item in vetor:
    print(f'{item:.2f}', end=' ')
