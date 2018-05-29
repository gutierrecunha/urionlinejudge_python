# -*- coding: utf-8 -*-
quantidade = int(input())
if quantidade >= 1 and quantidade < 10000:
    for i in range(0,quantidade):

        palavra = str(input())
        tamanho = len(palavra)
        palavras = list(palavra)
        metade = int(tamanho/2)
        novalista = []
            
        if tamanho <= 1000:
            for j in range(len(palavras)):
                if(ord(palavras[j]) >= 65 and ord(palavras[j]) <= 90 or ord(palavras[j]) >= 97 and ord(palavras[j]) <= 122):
                    palavras[j] = chr(ord(palavras[j]) + 3)
            for k in reversed(palavras):
                novalista.append(k)
            for z in range(metade, tamanho):
                novalista[z] = chr(ord(novalista[z]) -1)
                
            palavra = str.join('',novalista)
        
        
        print(palavra)