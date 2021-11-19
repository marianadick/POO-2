'''Implemente uma classe que, implementa algumas séries matemáticas importantes: Fibonacci,
Fatorial, Fibonarial, Primo. Use recursão para Fibonacci e Fatorial.'''

import math

class Funcoes():

    def fibonacci(n):
        utilitario_fibonacci = {0: 0, 1: 1}

        if n < 0:
            return '[Erro]: Entrada Inválida'

        elif n in utilitario_fibonacci:
            return utilitario_fibonacci[n]

        utilitario_fibonacci[n] = Funcoes.fibonacci(n-1) + Funcoes.fibonacci(n-2)
        return utilitario_fibonacci[n]

    def fatorial(n):
        if n == 1:
            return 1
        else:
            return (n * Funcoes.fatorial(n-1))

    def fibonarial(n):
        utilitario_fibonarial = 1
        for i in [Funcoes.fibonacci(x) for x in range(n+1)]:
            if i != 0:
                utilitario_fibonarial *= i
        return utilitario_fibonarial

    def primo(n):
        raiz = int(math.sqrt(n))
        if n in {0, 1}:
            return False
        for i in range(2, raiz+1):
            if n % i == 0:
                return False
        return True

def main():
    print([Funcoes.fibonacci(n) for n in range(9)])
    print(Funcoes.fibonacci(8))
    print(Funcoes.fibonarial(8))

    print(Funcoes.fatorial(5))

    print(Funcoes.primo(7))

main()