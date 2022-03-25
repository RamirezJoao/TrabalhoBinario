import numpy as np



def converter(lista):
    valores=[]
    ordenado = []
    dicionario = {}
    novo = {}
    codificado=[]
    texto=''
    numeros =[]
        
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
    print('\n')
    print('\n')
    return array

def decilambinario(a):
    algoritmos = []
    for i in a:
        p = 7
        for j in i:
            mult = j *(2**p)
            p -= 1
            algoritmos.append(mult)

    n=8

    output=[algoritmos[i:i + n] for i in range(0, len(algoritmos), n)]
    
    for i in range(len(output)):
        print(sum(output[i]))
            
    

a = converter([2,2,2,2,2,2,2,2,2,2,2,2])
print(a)
print('\n')
decilambinario(a)
