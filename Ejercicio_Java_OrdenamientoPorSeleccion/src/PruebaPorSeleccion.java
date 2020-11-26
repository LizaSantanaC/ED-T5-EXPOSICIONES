import java.util.Arrays;

class OrdenamientoPorSeleccion{
	public void ordenamientoSeleccion(int[] numeros) {
		for(int i = 0; i < numeros.length - 1; i++) {
			for(int j = i + 1; j < numeros.length; j++) {
				if(numeros[i] > numeros[j]) {
					int orden = numeros[i];
					numeros[i] = numeros[j];
					numeros[j] = orden;
				}
			}
		}
	}
}

public class PruebaPorSeleccion {
	public static void main(String[] args) {
		int[] numeros = {6, 1, 10, 2, 8, 4, 6, 9};
		OrdenamientoPorSeleccion ops = new OrdenamientoPorSeleccion();
		System.out.println("Or: " + Arrays.toString(numeros));
		ops.ordenamientoSeleccion(numeros);
		System.out.println("Numeros ordenados: " + Arrays.toString(numeros));
	}
}
