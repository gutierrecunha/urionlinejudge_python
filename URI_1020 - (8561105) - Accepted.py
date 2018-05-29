# -*- coding: utf-8 -*-

num = int(input())

ano = int(num / 365)
res1= num - (365*ano)

mes = int(res1 / 30)
res2= res1 - (30*mes)

dia = res2

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")