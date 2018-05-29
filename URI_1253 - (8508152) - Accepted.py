###### -*- coding: utf-8 -*-

quantidade = int(input())
for i in range(0,quantidade):

        palavra = str(input())
        tamanho = len(palavra)
        palavras = list(palavra)
        
        if tamanho <= 50:
            casas = int(input())
            if casas >= 0 or casas <=25:
                for j in range(len(palavras)):
                    pos=(ord(palavras[j]) - casas)
                    if(pos < 65):
                        pos=pos+26
                        palavras[j] = chr(pos)
                    else:
                        palavras[j] = chr(ord(palavras[j]) - casas)
                
                palavra = str.join('',palavras)
        
        print(palavra)