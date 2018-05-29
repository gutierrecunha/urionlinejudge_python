# -*- coding: utf-8 -*-

num = input().split( )
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

if (b>c and d>a and (c+d) > (a+b) and c >-1 and d >-1 and (a%2)==0 ):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

