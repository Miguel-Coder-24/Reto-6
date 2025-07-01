class PrimoValidador:
    def __init__(self, numeros):
        if not isinstance(numeros, list):
            raise TypeError("Se esperaba una lista de números.")

        for n in numeros:
            if not isinstance(n, int):
                raise ValueError(f"'{n}' no es un número entero válido.")

        self.numeros = numeros

    def es_primo(self, num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def obtener_primos(self):
        return [n for n in self.numeros if self.es_primo(n)]


# --- Ejecución del programa ---
try:
    entrada = input("Ingresa números separados por comas (ej: 2,3,4,5): ")
    numeros = list(map(int, entrada.split(",")))

    validador = PrimoValidador(numeros)
    primos = validador.obtener_primos()

    print("Números primos encontrados:", primos)

except ValueError as e:
    print(f"Entrada inválida: {e}")
except TypeError as e:
    print(f"Tipo incorrecto: {e}")
except Exception as e:
    print(f"Algo salió mal: {e}")
