class PalindromoValidador:
    def __init__(self, texto):
        """
        Inicializa el validador con un texto.

        Args:
            texto (str): Texto a verificar.

        Raises:
            TypeError: Si la entrada no es una cadena de texto.
            ValueError: Si la cadena está vacía o contiene solo espacios.
        """
        if not isinstance(texto, str):
            raise TypeError("La entrada debe ser una cadena de texto.")
        if texto.strip() == "":
            raise ValueError("La entrada no puede estar vacía.")

        self.texto_limpio = texto.replace(" ", "").lower()

    def es_palindromo(self):
        """
        Verifica si el texto es un palíndromo sin usar slicing.

        Returns:
            bool: True si es palíndromo, False si no.
        """
        invertido = ""
        for letra in self.texto_limpio:
            invertido = letra + invertido
        return self.texto_limpio == invertido


# --- Bloque de ejecución ---
try:
    entrada = input("Ingrese una palabra o frase: ")
    validador = PalindromoValidador(entrada)

    if validador.es_palindromo():
        print(f'"{entrada}" es un palíndromo.')
    else:
        print(f'"{entrada}" no es un palíndromo.')

except TypeError as e:
    print(f"Error de tipo: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
