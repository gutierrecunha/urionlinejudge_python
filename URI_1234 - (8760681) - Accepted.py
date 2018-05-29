# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
while True:
    try:
        frase = input()
        frase = frase.lower()
        lista = list(frase)
        cont = 0
        for i in range(len(frase)):
            if(ord(lista[i]) >= 65 and ord(lista[i]) <= 90 or ord(lista[i]) >= 97 and ord(lista[i]) <= 122) and cont == 0:
                lista[i] = lista[i].upper()
                cont +=1
            elif(ord(lista[i]) >= 65 and ord(lista[i]) <= 90 or ord(lista[i]) >= 97 and ord(lista[i]) <= 122) and cont == 1:
                cont = 0

        texto = ''.join(lista)
        print(texto)
    except:
        break