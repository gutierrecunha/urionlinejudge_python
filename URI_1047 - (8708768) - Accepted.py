# -*- coding: utf-8 -*-

num = input().split()
h1 = int(num[0])
m1 = int(num[1])
h2 = int(num[2])
m2 = int(num[3])

if h1==h2 and m1 ==m2:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if m1 <= m2:
        difMin = m2 - m1;
        flag = 1;
    if m1 > m2:
        difMin = 60 - (m1 - m2); 
        flag = -1;
    if h1 > h2:
        difHora = 24 - h1 + h2
    if h1 <= h2:
        difHora = h2 - h1;
    if flag > 0:
        horaFinal = difHora;
    else:
        if difHora == 0:
            horaFinal = 23;
        else:
            horaFinal = difHora - 1;
            
    print("O JOGO DUROU",horaFinal,"HORA(S) E",difMin,"MINUTO(S)");

