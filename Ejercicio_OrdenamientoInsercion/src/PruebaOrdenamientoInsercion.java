import java.util.Arrays;

interface Delay{
	public static void main(int mili) {
		try {
			Thread.sleep(mili);
		} catch (Exception e) {
			Thread.currentThread().interrupt();
		}
	}
}

class OrdenamientoInsercion{
	public void ordenamientoInsercion(int[] numeros) {
		int aux;
		for (int i = 1; i < numeros.length; i++) {
			aux= numeros[i];
				
			for (int j = 1 - 1; j > 0 && numeros[j] > aux; j--) {
				numeros[j + 1]= numeros[j];
				numeros[j]=aux;
			}
		}
	}
}

public class PruebaOrdenamientoInsercion {
	public static void main(String[] args) {
		int[] numeros= {5, 7, 11, 15, 4,12, 23, 3, 4, 2, 1, 45, 13};
		System.out.println("Números desordenados" + Arrays.toString(numeros));
		System.out.println("");
		OrdenamientoInsercion o= new OrdenamientoInsercion();
		o.ordenamientoInsercion(numeros);
		System.out.println("Números ordenados" + Arrays.toString(numeros));
	}
}
