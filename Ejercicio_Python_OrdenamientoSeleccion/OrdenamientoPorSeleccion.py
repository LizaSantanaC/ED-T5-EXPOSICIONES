class OrdenamientoPorSeleccion:
    def ordenamientoSeleccion(self, numeros):
        for i in range(len(numeros)):
            for j in range(i, len(numeros)):
                if(numeros[i] > numeros[j]):
                    minimo= numeros[i]
                    numeros[i]= numeros[j]
                    numeros[j]= minimo

oSeleccion= OrdenamientoPorSeleccion()
numeros= [3, 5, 1, 10, 12, 15, 11]
print("Numeros sin ordenar: " + str(numeros))
oSeleccion.ordenamientoSeleccion(numeros)
print("Numeros ordenados: " + str(numeros))