'''Exercicio 2: Escreva uma função que apaga do dicionário anterior, todas as palavras
que sejam ‘stopwords’. Ver https://gist.github.com/alopes/5358189'''

from exercicio_1 import dicionario

file = open(r'C:\Users\maria\Desktop\POO-2\Terceira Lista\exercicio_2.txt')
stopwords = file.read().split()

for stopword in stopwords:
    if stopword in dicionario:
        del dicionario[stopword]

print(dicionario)
print(f'Tamanho do dicionário: {len(dicionario)}')