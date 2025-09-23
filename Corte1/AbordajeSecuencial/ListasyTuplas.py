#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Crea una lista con 6 colores
#input()   # Espera entrada del usuario (aquí está comentado, no se ejecuta)
print(my_lista)   # Imprime toda la lista
print(type(my_lista))   # Imprime el tipo de dato (<class 'list'>)
print(my_lista[2])   # Imprime el elemento en la posición 2 (Amarillo, porque las posiciones empiezan en 0)

print("my_lista size: ", len(my_lista))   # Imprime el tamaño de la lista (6 elementos)
print(my_lista[0:2])   # Imprime los elementos desde el índice 0 hasta el 1 (['Rojo', 'Azul'])
print(my_lista[:2])    # Hace lo mismo que la línea anterior (['Rojo', 'Azul'])

my_lista.append('Blanco')      # Agrega 'Blanco' al final de la lista
print(my_lista)   # Imprime la lista actualizada

my_lista.insert(3, 'Negro')   # Inserta 'Negro' en la posición 3
print(my_lista)   # Muestra la lista con el nuevo elemento

my_lista.extend(['Marron', 'Gris'])   # Agrega los elementos de otra lista al final
print(my_lista)

print(my_lista.index('Azul'))   # Devuelve el índice donde está el elemento 'Azul' (posición 1)

#my_lista.remove('Magenta')   # Elimina 'Magenta' si existiera (comentado porque no está en la lista)
my_lista.remove('Marron')   # Elimina el primer 'Marron' que encuentre
print(my_lista)

my_lista.insert(8, 'Marron')   # Inserta 'Marron' en la posición 8
print(my_lista)

print(my_lista.pop())   # Elimina y devuelve el último elemento de la lista
size = len(my_lista)   # Guarda el tamaño actual de la lista
print("size = ", size)   # Imprime el tamaño
#print(my_lista.pop(size))   # Intento de eliminar en la posición "size", pero daría error (está comentado)

my_lista_3 = my_lista*3   # Repite la lista 3 veces
print("my_lista_3: ", my_lista_3)

print("Sort:")   # Texto informativo
print()
my_listaSort = my_lista.sort()   # Ordena la lista en orden alfabético, pero sort() devuelve None
print(my_listaSort)   # Imprime None (porque sort() no retorna la lista, solo la ordena internamente)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]   # Lista de números desordenados
print("Ordering my_NumList: ")   # Texto informativo
my_NumList.sort()   # Ordena la lista en forma ascendente
print(my_NumList)   # Muestra la lista ya ordenada

#OrderedLList = my_NumList.sort()   # Esto guardaría None, igual que arriba (comentado)
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)   # Ordena en forma descendente
print("De menor a mayor: ", my_NumList)   # Imprime la lista en orden descendente



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)   # Convierte la lista en una tupla (inmutable)
print()
print()
print("my_tuple: ", my_tupla)   # Imprime la tupla

print(my_tupla[0])   # Imprime el primer elemento de la tupla
print(my_tupla[2])   # Imprime el tercer elemento de la tupla

#Evaluar si un elemento está contenido en la tupla (Devuelve True o False)
print('Rojo' in my_tupla)   # Devuelve True si 'Rojo' está en la tupla
print(my_tupla.count('Rojo'))   # Cuenta cuántas veces aparece 'Rojo'

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')   # Esto NO es una tupla, es un string porque falta la coma
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999   # Crea una tupla automáticamente sin paréntesis
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla   # Se asigna cada valor de la tupla a una variable
print(nombre)   # Imprime 'Gaspar'
print(dia)      # Imprime 5
print(mes)      # Imprime 8
print(año)      # Imprime 1999

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)   # Imprime todo en formato texto

#Convertir una tupla en una lista
my_lista2 = list(my_tupla)   # Convierte la tupla en lista (ahora sí se puede modificar)
print(my_lista2)   # Imprime la lista
