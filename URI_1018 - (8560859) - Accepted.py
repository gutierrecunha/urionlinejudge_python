# -*- coding: utf-8 -*-

num = int(input())

nota_cem = int(num / 100)
res1= num - (100*nota_cem)

nota_cinquenta = int(res1 / 50)
res2= res1 - (50*nota_cinquenta)

nota_vinte = int(res2/20)
res3 = res2 - (20*nota_vinte)

nota_dez = int(res3/10)
res4 = res3 - (10*nota_dez)

nota_cinco = int(res4/5)
res5= res4 - (5*nota_cinco)

nota_dois = int(res5/2)
res6= res5 - (2*nota_dois)

nota_um = res6

print(num);
print(nota_cem, "nota(s) de R$ 100,00");
print(nota_cinquenta,"nota(s) de R$ 50,00");
print(nota_vinte,"nota(s) de R$ 20,00");
print(nota_dez,"nota(s) de R$ 10,00");
print(nota_cinco,"nota(s) de R$ 5,00");
print(nota_dois,"nota(s) de R$ 2,00");
print(nota_um,"nota(s) de R$ 1,00");