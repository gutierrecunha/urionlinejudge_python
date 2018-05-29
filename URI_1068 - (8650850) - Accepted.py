# -*- coding: utf-8 -*-

while True:
    try:
        expressao = input()
        cont=0
        cont1=0
        for i in range(len(expressao)):
            if expressao[i] == '(':
                cont+=1
            elif expressao[i] == ')':
                cont1+=1
            if(expressao[i] == ')' and cont < cont1):
                break
        if cont == cont1:
            print("correct")
        else:
            print("incorrect")
    except (EOFError):
        break   