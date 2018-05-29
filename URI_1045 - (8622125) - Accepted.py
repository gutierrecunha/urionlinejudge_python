# -*- coding: utf-8 -*-

num = input().split()
array =[]

for i in range (len(num)):
    array.append(float(num[i]))

array.sort( reverse=True )
A = array[0]
B = array[1]
C = array[2]

if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if (A**2) == ((B**2) + (C**2)):
        print("TRIANGULO RETANGULO")
    if (A**2) > ((B**2) + (C**2)):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < ((B**2) + (C**2)):
        print("TRIANGULO ACUTANGULO")
    if (A ==B and B==C):
        print("TRIANGULO EQUILATERO")
    if ((A == B) or (B == C) or (A == C)) and ((A != B) or (B != C) or (A != C)):
        print("TRIANGULO ISOSCELES")