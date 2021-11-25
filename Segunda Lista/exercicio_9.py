'''Exercício 9: Faça um Programa que leia um vetor A com 10 números inteiros, calcule
e mostre a soma dos quadrados dos elementos do vetor.'''

vetor = [int(x) for x in input().split()]
soma_dos_quadrados = 0

for item in vetor:
    soma_dos_quadrados += ((item)**2)

print(f'A soma dos quadrados dos itens do vetor é: {soma_dos_quadrados}')