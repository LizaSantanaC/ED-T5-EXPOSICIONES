def ordenamientoRadixSort(numeros, exp1):
    n= len(numeros)
    cantidadDatos= [0] * (n)
    contar= [0] * (10)
    for i in range(0, n):
        indice= (numeros[i]/exp1)
        contar[int((indice)%10)] += 1
    for i in range(1, 10):
        contar[i] += contar[i-1]
    i= n-1
    while i>=0:
        indice= (numeros[i]/exp1)
        cantidadDatos[contar[int((indice)%10)] - 1]= numeros[i]
        contar[int((indice)%10)] -= 1
        i -= 1
    i= 0

    for i in range(0, len(numeros)):
        numeros[i]= cantidadDatos[i]

def radixSort(numeros):
    max1 = max(numeros)
    exp = 1
    while max1/exp > 0:
        ordenamientoRadixSort(numeros, exp)
        exp *= 10

numeros= {170, 45, 75, 98, 24, 2, 9, 66}
print(f"NUmeros desordenados:  {numeros}")
radixSort(numeros)
print(f"NUmeros ordenados: {numeros}")