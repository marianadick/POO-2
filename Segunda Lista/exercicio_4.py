'''Exercício 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.'''

#Vou considerar as repetidas também, mas poderia ter utilizado set para contar apenas as consoantes únicas.

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes_lidas = []

vetor = [str(x).lower() for x in input().split()]

for item in vetor:
    if item not in vogais:
        consoantes_lidas.append(item)

if len(consoantes_lidas) == 0:
    print('Não encontramos nenhuma consoante.')
else:
    print(f'As {len(consoantes_lidas)} consoantes lidas foram:')
    print(', '.join(consoantes_lidas))
