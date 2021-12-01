'''Exercicio 4: Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde em um
dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta
da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O
campeão é o que tem a menor média de tempos.'''

resultados = {}
classificacao = {}
menor_volta = [99999, 0, 0]

def leitura_dos_dados():
    for _ in range(0, 6):
        nome_corredor = input('Insira o nome do corredor: ')
        count = 0
        media = 0
        resultados[nome_corredor] = []

        for _ in range(0, 10):
            count += 1
            volta = int(input(f'Insira o resultado (em segundos) da {count} volta: '))
            resultados[nome_corredor].append(volta)
            if volta < menor_volta[0]:
                menor_volta[0] = volta
                menor_volta[1] = count
                menor_volta[2] = nome_corredor
            media += volta
            classificacao[nome_corredor] = media

    return resultados

def classificacao_final():
    sort_classificacao = sorted(classificacao.items(), key=lambda x: x[1])
    count = 0
    for corredor in sort_classificacao:
        count += 1
        print(f'Em {count}o lugar: {corredor[0]}, com uma média de {(corredor[1]/10)} segundos.')
    
def imprime_menor_volta():
    print(f'A menor volta foi de {menor_volta[0]} s, na {menor_volta[1]} volta de {menor_volta[2]}')

def main():
    print(leitura_dos_dados())
    classificacao_final()
    imprime_menor_volta()

main()
