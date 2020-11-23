class OdenamientoPorInsercion:
    def ordenamientoInsercion(self, numeros):
    aux=0
    for i in range(1, len(numeros)):
        aux= numeros[i]
        j= (i-1)
        while(j >= 0 and numeros[j] > aux):
            numeros[j+1]= numeros[j]
            numeros[j]= aux
            j-=1

numeros= [5, 7, 11, 15, 4, 12, 23, 3, 4, 2, 1, 45, 13]
print("NUmeros desocrdenados:" + str(numeros))
o=OdenamientoPorInsercion()
o.ordenamientoInsercion(numeros)
print("Numeros ordenados:" + str(numeros))