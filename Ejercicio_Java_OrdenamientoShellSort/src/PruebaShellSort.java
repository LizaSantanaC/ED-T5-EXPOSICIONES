import java.util.Arrays;

class ShellSort{
	public void ordenamientoShellSort(int[] numeros) {
		int intervalo= numeros.length/2;
		while(intervalo > 0) {
			for (int i = 0; i < numeros.length; i++) {
				int j= i - intervalo;
				while (j >= 0) {
					int k= j + intervalo;
					if(numeros[j] <= numeros[k]) {
						j= -1;
					}else {
						int aux= numeros[j];
						numeros[j]= numeros[k];
						numeros[k]= aux;
						j-= intervalo;
					}
				}
			}
			intervalo= intervalo/2;
		}
	}
}

public class PruebaShellSort {
	public static void main(String[] args) {
		ShellSort shell= new ShellSort();
		int[] numeros= {12,58,1,59,47,36,4,3,6};
		System.out.println("Desordenado: " + Arrays.toString(numeros));
		shell.ordenamientoShellSort(numeros);
		System.out.println("Ordenado: " + Arrays.toString(numeros));
	}
}
