'''Exercicio 5: Escreva um programa para armazenar uma agenda de telefones usando
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o
nome completo da pessoa. Seu programa deve ter as seguintes funções:
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com
um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome. 
excluir_telefone – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da
agenda.
excluir_nome – essa função exclui uma pessoa da agenda.
consultar_telefone – essa função retorna os telefones de uma pessoa
na agenda'''

agenda = {}

def incluir_novo_nome(nome, telefones=[]):
    agenda[nome] = telefones

def incluir_telefone(nome, telefone):
    if nome in agenda.keys():
        agenda[nome].append(telefone)
    else:
        incluir = input('Esse nome ainda não se encontra na agenda. Gostaria de incluí-lo? [sim/não]')
        if incluir == 'sim':
            incluir_novo_nome(nome, [telefone])

def excluir_telefone(nome, telefone):
    if telefone in agenda[nome]:
        if len(agenda[nome]) > 1:
            agenda[nome].remove(telefone)
        else:
            del agenda[nome]
    else:
        return 'Esse telefone não consta na agenda!'

def excluir_nome(nome):
    if nome in agenda.keys():
        del agenda[nome]
    else:
        print('Pessoa não cadastrada na agenda')

def consultar_telefone(nome):
    if nome in agenda.keys():
        print(f' Os telefones de {nome} são {agenda[nome]}')
    else:
        print('Pessoa não cadastrada na agenda')


def main():
    incluir_novo_nome('Mariana', [48, 51])
    incluir_telefone('Mariana', 65)
    consultar_telefone('Mariana')
    excluir_telefone('Mariana', 65)
    consultar_telefone('Mariana')
    excluir_nome('Mariana')
    consultar_telefone('Mariana')

main()
