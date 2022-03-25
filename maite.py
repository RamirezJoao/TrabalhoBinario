# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:14:56 2022

@author: Aluno
"""

lista = [1,1,1,2,2,5,5,5,3,3]
valores=[]
ordenado = []
dicionario = {}
for i in lista:
    total = lista.count(i)
    valores.append(total)
for i,x in zip (lista,valores):
    dicionario[i] = x
print(dicionario)

for item in sorted(dicionario, key = dicionario.get, reverse=True):
    ordenado.append(dicionario[item])
print(ordenado)

    

   



