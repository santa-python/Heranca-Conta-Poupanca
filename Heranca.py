# -*- coding:utf-8 -*-
from Conta import Conta
from Poupanca import Poupanca

cc1 = Conta(500)
cc2 = Conta(1000)

cc1.doCredito(300)
cc2.doDebito(200)

cc1.doTransferencia(cc2, 200)
print('Saldo Conta 1: {} '.format(cc1.getSaldo()))
print('Saldo Conta 2: {} '.format(cc2.getSaldo()))

pp = Poupanca(300)
cc2.doTransferencia(pp, 250)

print('Saldo Conta 2 após transferência: {}'.format(cc2.getSaldo()))
print('Saldo Poupança após transferência: {}'.format(pp.getSaldo()))

pp.doCorrecao(0.65)

print('Poupança com Correção: {}'.format(pp.getSaldo()))