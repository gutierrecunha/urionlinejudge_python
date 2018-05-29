# -*- coding: utf-8 -*-
array =[]
array2 = []

quant = int(input())
for i in range(quant):
    num = int(input())
    array.append(num)
    if num not in array2:
        array2.append(num)
array2.sort()
for j in array2:
    print(j,"aparece", array.count(j),"vez(es)")