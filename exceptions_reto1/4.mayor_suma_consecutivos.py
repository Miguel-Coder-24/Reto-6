class SumaConsecutiva:
    def __init__(self, numeros):
        if not isinstance(numeros, list):
            raise TypeError("Se esperaba una lista de números.")

        if len(numeros) < 2:
            raise ValueError("Se necesitan al menos dos números para calcular la suma.")

        for n in numeros:
            if not isinstance(n, int):
                raise ValueError(f"'{n}' no es un número entero válido.")

        self.numeros = numeros

    def mayor_suma(self):
        mayor = self.numeros[0] + self.numeros[1]
        for i in range(len(self.numeros) - 1):
            suma = self.numeros[i] + self.numeros[i + 1]
            if suma > mayor:
                mayor = suma
        return mayor


# --- Bloque principal ---
try:
    entrada = input("Ingresa números separados por comas (ej: 4,6,1,9,2): ")
    lista = list(map(int, entrada.split(",")))

    calculadora = SumaConsecutiva(lista)
    resultado = calculadora.mayor_suma()

    print("La mayor suma entre dos elementos consecutivos es:", resultado)

except ValueError as e:
    print(f"Entrada inválida: {e}")
except TypeError as e:
    print(f"Tipo incorrecto: {e}")
except Exception as e:
    print(f"Algo salió mal: {e}")
