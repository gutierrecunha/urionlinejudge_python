# -*- coding: utf-8 -*-

quantidade = int(input())
for j in range(quantidade):
        expressao = input()
        cont=0
        cont1=0
        for i in range(len(expressao)):
            if expressao[i] == '<':
                cont+=1
            if expressao[i] == ">" and cont > 0:
                cont1 += 1
                cont -= 1
        print(cont1)