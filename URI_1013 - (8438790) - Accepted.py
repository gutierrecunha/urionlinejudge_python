# -*- coding: utf-8 -*-

Arr = input().split( )
A=int(Arr[0])
B=int(Arr[1])
C=int(Arr[2])

MaiorAB = (A + B + abs(A-B)) / 2;
MaiorC = (MaiorAB + C + abs(MaiorAB-C)) / 2;

print("{:.0f}".format(MaiorC),"eh o maior")