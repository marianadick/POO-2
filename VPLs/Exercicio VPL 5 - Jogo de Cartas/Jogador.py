from abc import ABC, abstractmethod
from operator import index
from Carta import *
from interfaces import AbstractJogador
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        carta = self.mao.pop()
        return carta

    @property
    def mao(self) -> list:
        return self.__mao

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.mao.append(carta)
