# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:07:14 2022

@author: emanu
"""

# def hoffman(lista):
lista=[1,3,3,3,6,4,2,2,2,2,2,2,2,8,8,8,8]
lista2=[]
for elemento in lista:
    lista2.append(lista.count(elemento))
dic = {}
for i,y in zip(lista, lista2):
    dic[i] = y
    
lista3 = list(zip(dic.keys(),dic.values()))
lista3.sort(key=lambda x: x[1])
dic1 = dict((z, w) for (z, w) in lista3)
print(dic1,'\n')

maior = dic[max(dic1, key=dic1.get)]

for n, a in dic.items():
    if a == maior: 
        principal=n
        print(principal)
        



