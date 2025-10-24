
# Clase Calculadora

class Calculadora:
    # Constructor de la clase (no inicializa nada por ahora)
    def __init__(self):
        pass

    # Método para sumar dos números
    def sumar(self, a, b):
        return a + b

    # Método para restar dos números
    def restar(self, a, b):
        return a - b

    # Método para multiplicar dos números
    def multiplicar(self, a, b):
        return a * b

    # Método para dividir dos números
    def dividir(self, a, b):
        # Se verifica que el divisor no sea cero para evitar error
        if b == 0:
            return "Error: división entre cero"
        return a / b

    # Método para calcular una potencia sin usar librerías
    def potencia(self, base, exponente):
        resultado = 1  # Se inicializa el resultado en 1

        # Si el exponente es cero, cualquier número elevado a 0 da 1
        if exponente == 0:
            return 1

        # Si el exponente es positivo
        elif exponente > 0:
            # Se multiplica la base por sí misma tantas veces como indique el exponente
            for _ in range(exponente):
                resultado *= base

        # Si el exponente es negativo
        else:
            # Se multiplica la base el número de veces indicado por el valor absoluto del exponente
            for _ in range(-exponente):
                resultado *= base
            # Luego se toma el recíproco (1 dividido entre el resultado)
            resultado = 1 / resultado

        # Se retorna el resultado final
        return resultado

    # Método para calcular la raíz cuadrada usando el método de Newton-Raphson
    def raiz_cuadrada(self, numero):
        # Se verifica que el número no sea negativo
        if numero < 0:
            return "Error: raíz de número negativo"

        # Estimación inicial
        aproximacion = numero / 2

        # Se repite el proceso 20 veces para mejorar la precisión
        for _ in range(20):
            # Fórmula del método de Newton-Raphson:
            # x(n+1) = (x(n) + n/x(n)) / 2
            aproximacion = (aproximacion + numero / aproximacion) / 2

        # Se retorna la aproximación obtenida
        return aproximacion

    # Método para calcular el factorial de un número entero positivo
    def factorial(self, n):
        # Verifica si el número es negativo (no existe factorial para negativos)
        if n < 0:
            return "Error: factorial no definido para negativos"

        # Se inicializa el resultado en 1
        resultado = 1

        # Se multiplica por todos los enteros desde 1 hasta n
        for i in range(1, n + 1):
            resultado *= i

        # Se retorna el resultado final del factorial
        return resultado



# Clase para calcular áreas de figuras geométricas


class Figuras:
    # Método para calcular el área de un cuadrado
    def area_cuadrado(self, lado):
        return lado * lado

    # Método para calcular el área de un rectángulo
    def area_rectangulo(self, base, altura):
        return base * altura

    # Método para calcular el área de una circunferencia (círculo)
    def area_circunferencia(self, radio):
        pi = 3.1416  # Se usa una aproximación manual de π
        return pi * radio * radio

    # Método para calcular el área de un triángulo rectángulo
    def area_triangulo_rectangulo(self, base, altura):
        return (base * altura) / 2



# Bloque principal (ejecución del programa)

if __name__ == "__main__":
    # Se crean objetos de ambas clases
    calc = Calculadora()
    figuras = Figuras()

    # Ejemplos de uso de la clase Calculadora
    print("Potencia  =", calc.potencia(5, 3))
    print("Raíz cuadrada  =", calc.raiz_cuadrada(144))
    print("Factorial  =", calc.factorial(7))

    # Ejemplos de uso de la clase Figuras
    print("Área del cuadrado  =", figuras.area_cuadrado(5))
    print("Área del rectángulo  =", figuras.area_rectangulo(4, 9))
    print("Área de la circunferencia  =", figuras.area_circunferencia(9))
    print("Área del triángulo rectángulo  =", figuras.area_triangulo_rectangulo(7, 4))
