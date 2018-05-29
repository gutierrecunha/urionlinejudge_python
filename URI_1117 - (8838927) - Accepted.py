# -*- coding: utf-8 -*-

nota=[]
cont=0
while True:
    
    if cont <2:
        num = float(input())
    else:
        break
    if num<0 or num>10:
        print("nota invalida")
    else:
        nota.append(num)
        cont+=1

media = (nota[0]+nota[1])/2
print("media = {:.2f}".format(media))