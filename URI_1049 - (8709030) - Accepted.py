# -*- coding: utf-8 -*-

reino1 = input()
reino2 = input()
reino3 = input()

if reino1 == "vertebrado":
    if reino2 == "ave":
        if reino3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if reino3 == "onivoro":
            print("homem")
        else:
            print("vaca")
        
elif reino1 == "invertebrado":
    if reino2 == "inseto":
        if reino3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if reino3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
    
