# -*- coding: utf-8 -*-

x = y = 0
num = input().split()
x = float(num[0])
y = float(num[1])

if x==0 and y==0:
    print("Origem")
elif x==0 and y!=0:
    print("Eixo Y")
elif x!=0 and y==0:
    print("Eixo X")
elif x>0 and y>0:
    print("Q1")
elif x>0 and y<0:
    print("Q4")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")