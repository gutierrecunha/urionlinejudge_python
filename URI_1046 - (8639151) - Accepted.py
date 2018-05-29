# -*- coding: utf-8 -*-

num = input().split()

h_ini = int(num[0])
h_fim = int(num[1])

if h_ini < h_fim:
    val = h_fim - h_ini
elif h_ini > h_fim:
    val = 24 - h_ini + h_fim
else:
    val = 24
print("O JOGO DUROU",val,"HORA(S)")