# -*- coding: utf-8 -*-

num = input().split()
A = float(num[0])
B = float(num[1])
C = float(num[2])

if (A<(B+C) and C<(A+B)and B<(A+C)):
    perimitro=A+B+C
    print("Perimetro = {:.1f}".format(perimitro))
else:
    area = ((A + B) * C) / 2
    print("Area = {:.1f}".format(area))