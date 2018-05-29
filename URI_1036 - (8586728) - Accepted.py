# -*- coding: utf-8 -*-

num = input().split()
A = float(num[0])
B = float(num[1])
C = float(num[2])

if A == 0:
    print("Impossivel calcular")
else:
    delta = B**2 - (4*A*C)
    
    if delta < 0.0:
        print("Impossivel calcular")
    else:
        raiz = delta ** 0.5
        r1 = (-B+raiz)/(2*A)
        r2 = (-B-raiz)/(2*A)
        print("R1 = {:.5f}".format(r1))
        print("R2 = {:.5f}".format(r2))