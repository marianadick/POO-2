'''Exercício 7: Faça um Programa que leia um vetor de 5 números inteiros, mostre a
soma, a multiplicação e os números.'''

import functools

vetor = [int(x) for x in input().split()]
soma = functools.reduce(lambda a, b: a+b, vetor)
mult = functools.reduce(lambda a, b: a*b, vetor)

print(f'Números: {vetor}')
print(f'Soma: {soma}')
print(f'Multiplicação: {mult}')