class PruebaQuickSort:

    def OrdenamientoQuickSort(self, numeros, izq, der):
        pivote= numeros[izq]
        i= izq
        j= der
        aux= 0
        while i < j:
            while numeros[i] <= pivote and i<j:
                i += 1
            while numeros[j] > pivote:
                j -= 1
            if i < j:
                aux= numeros[i]
                numeros[izq]= numeros[j]
                numeros[j]= pivote
            if izq < j-1:
                self.OrdenamientoQuickSort(numeros, izq, j-1)
            if j+1 < der:
                self.OrdenamientoQuickSort(numeros, j+1, der)

quicksort= PruebaQuickSort();
numeros= [10, 12, 5, 2, 8, 3, 1, 7, 22, 6, 30, 4, 11, 2, 9]
print("Desordenado: " + str(numeros))
quicksort.OrdenamientoQuickSort(numeros, 0, len(numeros) - 1)
print("Ordenado: " + str(numeros))