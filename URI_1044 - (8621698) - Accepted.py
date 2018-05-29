# -*- coding: utf-8 -*-

num = input().split()
A = int(num[0])
B = int(num[1])

if ( A%B == 0 or B%A == 0 ):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")