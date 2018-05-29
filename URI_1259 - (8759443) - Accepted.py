# -*- coding: utf-8 -*-

quant = int(input())
listnumpar = []
listnumimpar = []

for i in range(quant):
    num = int(input())
    if num%2==0:
        listnumpar.append(num)
    else:
        listnumimpar.append(num)
    
listnumpar.sort()
listnumimpar.sort(reverse=True)
listnum = listnumpar + listnumimpar

for j in range(len(listnum)):
    print(listnum[j])