# -*- coding: utf-8 -*-

while True:
    passos = input().split(" ")
    x1 = int(passos[0])
    y1 = int(passos[1])
    x2 = int(passos[2])
    y2 = int(passos[3])
    
    cont=0
    
    if (x1*y1*x2*y2)==0:
        break
    if(x1==x2 and y1==y2):
        cont=0
    elif(x1==x2 or y1==y2):
        cont = cont + 1
    else:
        res = abs((y2-y1)/(x2-x1))
        if res==1:
            cont = cont + 1
        else:
            cont = cont + 2
        
    print(cont)