def funcion_aritmetica(num1, num2, operador): 
    """Realiza operaciones básicas entre dos números"""
    try:
        if operador == "+":  # Suma
            return num1 + num2
        elif operador == "-":  # Resta
            return num1 - num2
        elif operador == "*":  # Multiplicación
            return num1 * num2
        elif operador == "/":  # División
            return num1 / num2  # Puede lanzar ZeroDivisionError
        else:
            raise ValueError("Operador no válido. Use: +, -, * o /")
    except ZeroDivisionError:
        return "Error: división por cero"
    except TypeError:
        return "Error: los operandos deben ser números"
    except ValueError as ve:
        return f"Error: {ve}"

# Programa principal
print("Bienvenido a la calculadora")
print("Operaciones disponibles: +, -, *, /")

try:
    entrada = input("Ingrese los dos números y el operador separados por comas (ejemplo: 5,3,+): ")
    num1_str, num2_str, operador = entrada.split(",")  # Puede lanzar ValueError si no hay 3 partes

    num1 = int(num1_str.strip())  # Conversión segura con .strip()
    num2 = int(num2_str.strip())

    resultado = funcion_aritmetica(num1, num2, operador.strip())  # Llama a la función
    print("El resultado de la operación es:", resultado)

except ValueError:
    print("Error: debe ingresar dos números y un operador separados por comas (ej: 5,3,+).")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
