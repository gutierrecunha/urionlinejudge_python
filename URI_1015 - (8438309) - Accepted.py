# -*- coding: utf-8 -*-

p1 = input().split( )
X1=float(p1[0])
Y1=float(p1[1])

p2 = input().split( )
X2=float(p2[0])
Y2=float(p2[1])

print("{:.4f}".format(((X2 ** 2 - (2 * X2 * X1) + X1 **2) + (Y2 ** 2 - (2 * Y2 * Y1) + Y1 **2)) ** (1/2)))