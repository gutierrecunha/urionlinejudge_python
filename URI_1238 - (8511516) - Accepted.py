# -*- coding: utf-8 -*-

quantidade = int(input())
for i in range(0,quantidade):
    palavras = input().split()
    palavra1 = list(palavras[0])
    palavra2 = list(palavras[1])
    tamA = len(palavra1)
    tamB = len(palavra2)
    novalista = []

    
    if tamA >= 1 and tamA <= 50 and tamB >= 1 and tamB <= 50:
        maior = int((tamA + tamB + abs(tamA-tamB)) / 2)
        if tamA >= 1 and tamA <= 50 and tamB >= 1 and tamB <= 50:
            for i in range(0,maior):
                if tamA > tamB:
                    if tamB > 0:
                        novalista.append(palavra1[i])
                        novalista.append(palavra2[i])
                        tamB = tamB-1
                    else:
                        novalista.append(palavra1[i])
                else:
                    if tamA > 0:
                        novalista.append(palavra1[i])
                        novalista.append(palavra2[i])
                        tamA = tamA-1
                    else:
                        novalista.append(palavra2[i])
                        
    palavras = str.join('',novalista)
    print (palavras)
    