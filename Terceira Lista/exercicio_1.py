'''Exercício 1: Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a palavra considerada.'''

dicionario = {}

file = open(r'C:\Users\maria\Desktop\POO-2\Terceira Lista\exercicio_1.txt')
texto = file.read().lower()

texto = texto.replace(',', '')
texto = texto.replace('.', '')
palavras = texto.split()

for palavra in palavras:
    if palavra not in dicionario:
        dicionario[palavra] = palavras.count(palavra)

print(dicionario)
print(f'Tamanho do dicionário: {len(dicionario)}')
