'''Exercício 1: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

vetor = [int(x) for x in input().split()]

for item in vetor:
    print(item, end=' ')
