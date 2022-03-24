from collections import Counter


def binario(x):
    
    valores = []
    x.sort()
    print(x)
    total = Counter(x)
    print(total)
    
    for i in total:
        valores.append(total[i])
        print(total[i])
        
    valores.sort(reverse = True)
    print(valores)
    
    



lista = [1,1,1,1,1,2,2,2,2,3,3,3,3,2,2,2,2,3,3,4,4,4]
binario(lista)