# -*- coding:utf-8 -*-

class Conta:
    saldo = 0.0

    def __init__(self, valor):
        self.setSaldo(valor)
    
    def doCredito(self, valor):
        self.setSaldo(self.getSaldo() + valor)
    
    def doDebito(self, valor):
        self.setSaldo(self.getSaldo() - valor)

    def doTransferencia(self, outra, valor):
        self.doDebito(valor)
        outra.doCredito(valor)

    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo