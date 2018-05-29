# -*- coding: utf-8 -*-

while True:
    quant = int(input())

    if quant == 0:
        break
   
    num = list(map(int,input().split()))
        
    print("Mary won",num.count(0),"times and John won",num.count(1),"times")