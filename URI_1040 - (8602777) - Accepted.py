# -*- coding: utf-8 -*-

num = input().split()
A = float(num[0])
B = float(num[1])
C = float(num[2])
D = float(num[3])
calc = 0.0
E = 0.0

MEDIA = ((2 * A) + (3 * B) + (4 * C) + (1 * D))/10

print("Media: {:.1f}".format(MEDIA))
if MEDIA >= 7.0:
    print("Aluno aprovado.")
elif MEDIA < 5.0:
    print("Aluno reprovado.")
elif MEDIA >=5.0 and MEDIA <= 6.9:
    print("Aluno em exame.")
    num1 = input().split()
    E = float(num1[0])
    print("Nota do exame: {:.1f}".format(E))
    calc = (E + MEDIA)/2
    if calc >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print("Media final: {:.1f}".format(calc))