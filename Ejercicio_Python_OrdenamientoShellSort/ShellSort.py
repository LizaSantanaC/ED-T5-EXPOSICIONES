class ShellSort:
    def ordenamientoShellSort(self, numeros):
        intervalo= len(numeros)/2
        intervalo= int(intervalo)
        while(intervalo > 0):
            for i in range (int(intervalo), len(numeros)):
                j= i - int(intervalo)
                while(j >=0):
                    k= j + int(intervalo);
                    if(numeros[j] <= numeros[k]):
                        j-=1
                    else:
                        aux= numeros[j]
                        numeros[j]= numeros[k]
                        numeros[k]= aux
                        j-= int(intervalo)
            intervalo= int(intervalo)/2

shellSort= ShellSort()
numeros= {12,58,1,59,47,36,4,3,6}
print(f"Desordenado: {numeros}")
shellSort.ordenamientoShellSort(numeros)
print(f"Ordenados: {numeros}")