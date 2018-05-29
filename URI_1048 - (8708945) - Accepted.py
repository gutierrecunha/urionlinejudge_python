# -*- coding: utf-8 -*-

salario = float(input())

if salario >=0  and salario <= 400.00:
    porcentagem = 15
    reajuste = (salario * porcentagem)/100
    novosalario = salario + reajuste
    
elif salario >=400.01  and salario <= 800.00:
    porcentagem = 12
    reajuste = (salario * porcentagem)/100
    novosalario = salario + reajuste
    
elif salario >=800.01  and salario <= 1200.00:
    porcentagem = 10
    reajuste = (salario * porcentagem)/100
    novosalario = salario + reajuste
    
elif salario >=1200.01  and salario <= 2000.00:
    porcentagem = 7
    reajuste = (salario * porcentagem)/100
    novosalario = salario + reajuste

elif salario >2000.00:
    porcentagem = 4
    reajuste = (salario * porcentagem)/100
    novosalario = salario + reajuste
    

print("Novo salario: {:.2f}".format(novosalario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual:", porcentagem,"%")
