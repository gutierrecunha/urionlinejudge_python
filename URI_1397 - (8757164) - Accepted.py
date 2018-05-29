# -*- coding: utf-8 -*-

while True:
    
    quant = int(input())
    contA = 0
    contB = 0
    contEmpate = 0
    
    
    if quant == 0:
        break

    for i in range(quant):
        num = input().split()        
        A = int(num[0])
        B = int(num[1])
        
        if A == B:
            contEmpate=contEmpate-1
        else:
            MaiorAB = (A + B + abs(A-B)) / 2
            contEmpate=0
            
            if MaiorAB == A:
                contA+=1
                contEmpate=0
            else:
                contB+=1
    if contEmpate <=0:
        print(contA,contB)      
    else:
        print("0 0")
    