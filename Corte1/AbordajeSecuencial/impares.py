#Este ejercicio vale 1 decima del primer corte

while True:
    try:
       numero = int(input("Ingresa un número: "))
       if numero % 2 == 0:
          print(f"{numero} es par")
       else:
          print(f"{numero} es impar")
    except ValueError:
     print("Ingresa un número válido")
       
    except KeyboardInterrupt:
      print("\nAdiós <3")
      break        