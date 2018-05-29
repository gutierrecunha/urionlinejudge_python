# -*- coding: utf-8 -*-

num = input().split()
A = int(num[0])
B = int(num[1])
soma = 0
tabela = [4.00,4.50,5.00,2.00,1.50]
A = A-1
for i in range(B):
    soma = soma + tabela[A]
print("Total: R$ {:.2f}".format(soma))