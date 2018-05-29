# -*- coding: utf-8 -*-

while True:
    try:
        num = input().split()
        A = int(num[0])
        B = int(num[1])
        C = int(num[2])
        
        if A == B == C:
            print('*')
        elif A == B:
            print('C')
        elif B == C:
            print('A')
        else:
            print('B')


    except (EOFError):
        break
    