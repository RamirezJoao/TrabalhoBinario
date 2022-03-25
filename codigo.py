# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:52:13 2022

@author: Aluno
"""
import numpy as np
lista =[2,2,2,2,2,2,2,2,2,2,2,2]
valores=[]
ordenado = []
dicionario = {}
novo = {}
codificado=[]
texto=''
numeros =[]
lista_qualquercoisa = []
    
for i in lista:
    total = lista.count(i)
    valores.append(total)
for i,x in zip (lista,valores):
    dicionario[i] = x

for item in sorted(dicionario, key = dicionario.get, reverse=True):
    ordenado.append(item)

txt = "0"
for i in ordenado:
    novo[i] = txt
    txt = "1"+txt
    
for j in lista:
    codificado.append((novo[j]))

for g in codificado:
    texto+=g

texto = list(texto)

           
while True:
    verificar = len(texto)%8

    if verificar == 0: 
        break
        
    else:
        texto.append('1')
        
for i in texto:
    numeros.append(int(i))   
colunas = int(len(texto)/8)
array = np.array(numeros)
array = array.reshape((colunas , 8))
for i in array:
    for j in i:
        lista_qualquercoisa.append(j)
        

lista_qualquercoisa = ''.join(lista_qualquercoisa) 
print(lista_qualquercoisa)
