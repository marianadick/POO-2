'''Exercício 5: Faça um Programa que leia 20 números inteiros e armazene-os num
vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor
impar. Imprima os três vetores.'''

vetor = [int(x) for x in input().split()]

pares = list(filter(lambda x: x % 2 == 0, vetor))
impares = list(filter(lambda x: x % 2 == 1, vetor))

print(f'Vetor de entrada {vetor}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
