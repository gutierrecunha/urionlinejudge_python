# -*- coding: utf-8 -*-

quant = int(input())
for i in range(quant):
    num = input().split()
    a = list(num[0])
    b = list(num[1])
    if len(a) > len(b):
        d = len(a) - len(b)
    else:
        d = len(b) - len(a)
    c = a[d:]
    if b == c:
        print("encaixa")
    else:
        print("nao encaixa")
