# -*- coding: utf-8 -*-


num = input().split(".")
nota = int(num[0])
centavos = int(num[1])

nota_cem = int(nota / 100)
res1= nota - (100*nota_cem)

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

moeda_um = res6

moeda_cinquenta = int(centavos/50)
res8= centavos - (50*moeda_cinquenta)

moeda_vintecinco = int(res8/25)
res9= res8 - (25*moeda_vintecinco)

moeda_dez = int(res9/10)
res10= res9 - (10*moeda_dez)

moeda_cinco = int(res10/5)
res11= res10 - (5*moeda_cinco)

moeda_umcentavo = int(res11)

print("NOTAS:")
print(nota_cem, "nota(s) de R$ 100.00")
print(nota_cinquenta,"nota(s) de R$ 50.00")
print(nota_vinte,"nota(s) de R$ 20.00")
print(nota_dez,"nota(s) de R$ 10.00")
print(nota_cinco,"nota(s) de R$ 5.00")
print(nota_dois,"nota(s) de R$ 2.00")

print("MOEDAS:")
print(moeda_um, "moeda(s) de R$ 1.00")
print(moeda_cinquenta,"moeda(s) de R$ 0.50")
print(moeda_vintecinco,"moeda(s) de R$ 0.25")
print(moeda_dez,"moeda(s) de R$ 0.10")
print(moeda_cinco,"moeda(s) de R$ 0.05")
print(moeda_umcentavo,"moeda(s) de R$ 0.01")