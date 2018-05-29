# -*- coding: utf-8 -*-

num = int(input())

hora = int(num / 3600)
res1= num - (3600*hora)

minuto = int(res1 / 60)
res2= res1 - (60*minuto)

segundo = res2

print(str(hora)+":"+str(minuto)+":"+str(segundo))