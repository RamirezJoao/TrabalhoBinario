# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hoffman(lista):
    lista2=[]
    dic={}
    for i in lista:
         lista2.append(lista.count(i))
    dic = {}
    for i,x in zip(lista, lista2):
        dic[x] = i
        print(dic) 

hoffman([1,3,3,3,6,4,2,2,2,2,2,2,2,8,8,8,8,4,4,4])


        
