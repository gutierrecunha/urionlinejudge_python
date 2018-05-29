# -*- coding: utf-8 -*-

leds={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
quantidade = int(input())
for i in range(0,quantidade):
    num = input()
    cont=0
    for j in num:
        cont=cont+leds[int(j)]
            
    print("%d leds" %int(cont))