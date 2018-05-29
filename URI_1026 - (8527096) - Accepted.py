# -*- coding: utf-8 -*-

while True:
    try:
        palavra = input().split(" ")
        a = int(palavra[0])
        b = int(palavra[1])
        
        print (a^b)
    except (EOFError):
        break