# -*- coding:utf-8 -*-
from Conta import Conta

class Poupanca(Conta):
    def __init__(self, valor):
        Conta.__init__(self, valor)
        self.setSaldo(valor)

    def doCorrecao(self, percentual):
        self.setSaldo(self.getSaldo() + self.getSaldo() * percentual / 100)