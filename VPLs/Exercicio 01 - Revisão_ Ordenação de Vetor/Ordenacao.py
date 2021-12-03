"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar: list):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_in = array_para_ordenar
        
    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        l = len(self.array_in)
        for i in range(l):
            for j in range(l-i-1):
                if self.array_in[j] > self.array_in[j+1]:
                    self.array_in[j], self.array_in[j+1] = self.array_in[j+1], self.array_in[j]
        
        return self.array_in


    def toString(self):
        """Converte o conteudo do array em String formatado"""
        for i in range(len(self.array_in)):
            self.array_in[i] = str(self.array_in[i])
        array_out = ",".join(self.array_in)
        
        return array_out