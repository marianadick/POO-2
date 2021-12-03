from operator import index
from interfaces import AbstractControladorJogo
from interfaces import Tipo
import Personagem, Carta, Jogador, Mesa
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if isinstance(tipo, Tipo):
            personagem = Personagem(energia, habilidade, velocidade,
                                    resistencia, tipo)
            self.personagems.append(personagem)
            return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if personagem in self.personagems:
            carta = Carta(personagem)
            self.baralho.append(carta)
            return carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        if isinstance(jogador1, Jogador) and isinstance(jogador2, Jogador):
            i1 = random.randint(0, len(self.baralho))
            i2 = random.randint(0, len(self.baralho))
            for i in range(0, 5):
                jogador1.inclui_carta_na_mao(self.baralho[i1])
                jogador2.inclui_carta_na_mao(self.baralho[i2])

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            if (mesa.carta_jogador1.valor_total_carta() >
                    mesa.carta_jogador2.valor_total_carta()):
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            elif (mesa.carta_jogador1.valor_total_carta() <
                    mesa.carta_jogador2.valor_total_carta()):
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            else:
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)

            if len(mesa.jogador1.mao) == 0:
                return mesa.jogador2
            elif len(mesa.jogador2.mao) == 0:
                return mesa.jogador1
            else:
                return None
