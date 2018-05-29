# -*- coding: utf-8 -*-

quantidade = int(input())
if quantidade < 1001:
    for i in range(0,quantidade):

        palavra = str(input())
        palavra = palavra.lower()
        tamanho = len(palavra)
        
        if tamanho == 3:
            palavras = list(palavra)
            one = ['o','n','e']
            two = ['t','w','o']       
            cont_one=0
            cont_two=0
            for i in range(len(palavras)):
                if palavras[i]==one[i]:
                    cont_one+=1
                elif palavras[i]==two[i]:
                    cont_two+=1
            if cont_one >=2:
                print("1")
            elif cont_two >=2:
                print("2")
        elif tamanho == 5:
            print("3")