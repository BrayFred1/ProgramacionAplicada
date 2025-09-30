#Este ejercicio vale 1 decima del primer corte
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
      try:
            numero = int(input("Ingrese un número: "))
            if es_primo(numero):
                  print(f"{numero} es primo")
            else:
                  print(f"{numero} no es primo")
      except ValueError:
            print("Ingrese un número válido")
      except KeyboardInterrupt:
            print("Adiós <3")

            break
                 

