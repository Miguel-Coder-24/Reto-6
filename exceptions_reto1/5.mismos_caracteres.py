class ComparadorCaracteres:
    def __init__(self, palabras):
        if not isinstance(palabras, list):
            raise TypeError("Se esperaba una lista de palabras.")
        if not all(isinstance(p, str) for p in palabras):
            raise ValueError("Todos los elementos deben ser cadenas de texto.")
        if any(p.strip() == "" for p in palabras):
            raise ValueError("Las palabras no pueden estar vacías.")
        self.palabras = [p.strip() for p in palabras]  # Limpiar espacios

    def con_mismos_caracteres(self):
        resultado = []
        for palabra in self.palabras:
            for otra in self.palabras:
                if palabra != otra and set(palabra) == set(otra):
                    resultado.append(palabra)
                    break  # Basta encontrar una coincidencia
        return list(set(resultado))  # Eliminar duplicados


# --- Uso con manejo de errores ---
try:
    entrada = input("Ingresa palabras separadas por comas (ej: 'roma,amor,maro'): ")
    lista_palabras = entrada.split(",")

    comparador = ComparadorCaracteres(lista_palabras)
    coincidencias = comparador.con_mismos_caracteres()

    print("Palabras con los mismos caracteres:", coincidencias)

except TypeError as e:
    print(f"Error de tipo: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
