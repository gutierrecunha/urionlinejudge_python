# -*- coding: utf-8 -*-

while True:
    tempo = input().split(" ")
    h1 = int(tempo[0])
    m1 = int(tempo[1])
    h2 = int(tempo[2])
    m2 = int(tempo[3])
    hora_inicio=0
    hora_final=0
    if h1==0 and m1==0 and h2==0 and m2==0:
        break
    if h1 == 0:
        hora_inicio = 1440 + m1
    else:
        hora_inicio = h1*60 + m1
    if h2 == 0:
        hora_final = 1440 + m2
    else:
        hora_final = h2*60 + m2
    if (hora_final > hora_inicio):
        despertar = hora_final-hora_inicio
    else:
        despertar = 1440 -(hora_inicio - hora_final)
    
    print(despertar)