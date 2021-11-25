'''Exercício 10: Faça um Programa que leia dois vetores com 10 elementos cada. Gere
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.'''

vetor1 = [int(x) for x in input().split()]
vetor2 = [int(x) for x in input().split()]
vetor3 = [*sum(zip(vetor1,vetor2),())]

print(f'Primeiro vetor: {vetor1}')
print(f'Segundo vetor: {vetor2}')
print(f'Vetor intercalado: {vetor3}')
