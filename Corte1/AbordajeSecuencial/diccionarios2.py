# #### Get A Key
# #you can access the values in it by providing the key:

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# # Diccionario con edificios y sus alturas.

# print(building_heights["Burj Khalifa"]) # Prints 828
# # Accede al valor de la clave "Burj Khalifa" (828).

# print(building_heights["Ping An"]) # Prints 599
# # Accede al valor de la clave "Ping An" (599).

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# # Diccionario con elementos zodiacales como claves y listas de signos como valores.

# print(zodiac_elements["earth"])
# # Imprime ["Taurus", "Virgo", "Capricorn"]

# print(zodiac_elements["fire"])
# # Imprime ["Aries", "Leo", "Sagittarius"]

# ## Get an Invalid Key

# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# # Vuelve a definir el diccionario de edificios.

# print(building_heights["Landmark 81"])

# ##One way to avoid this error is to first check if the key exists in the dictionary:
# key_to_check = "Landmark 81"

# if key_to_check in building_heights:
#   print(building_heights["Landmark 81"])
# # Verifica si la clave existe antes de acceder, evitando error.

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# # Redefine el diccionario zodiac_elements.

# zodiac_elements["energy"] = "Not a Zodiac element"
# # Agrega una nueva clave "energy" al diccionario.

# if "energy" in zodiac_elements:
#   print(zodiac_elements["energy"])
# # Comprueba que existe y la imprime ("Not a Zodiac element").

# ##Safely Get a Key
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# building_heights.get("Shanghai Tower")
# # Devuelve 632 (sin error si existe la clave).

# building_heights.get("My House")
# # Devuelve None (si no existe la clave).

# ###
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# # Diccionario de usuarios y sus IDs.

# user_ids.get("teraCoder")
# # Devuelve 100019.

# if user_ids.get("teraCoder") == None:
#    tc_id = 1000
# else: 
#    tc_id = user_ids.get("teraCoder")
# # Asigna tc_id con el valor de "teraCoder" o 1000 si no existe.

# print(tc_id)
# # Imprime 100019.

# if user_ids.get("superStackSmash") == None:
#      stack_id = 100000
# # Si no existe "superStackSmash", asigna 100000.

# print(stack_id)
# # Imprime 100000.

# ###Delete a Key
# .pop() works to delete items from a dictionary, when you know the key value.
# raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# print(raffle.pop(320291, "No Prize"))
# # Elimina clave 320291 y devuelve "Gift Basket".

# print(raffle)
# # Imprime el diccionario sin esa entrada.

# print(raffle.pop(100000, "No Prize"))
# # Como no existe 100000, devuelve "No Prize".

# print(raffle)
# # Diccionario sigue igual.

# print(raffle.pop(872921, "No Prize"))
# # Elimina clave 872921 y devuelve "Concert Tickets".

# print(raffle)
# # Imprime diccionario actualizado.

# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
# # Diccionario con ítems y puntos de salud.

# health_points = 20
# # Puntos de salud iniciales.

# health_points += available_items.pop("stamina grains", 0)
# # Suma 15 a health_points y elimina "stamina grains" del diccionario.

# health_points += available_items.pop("power stew", 0)
# # Suma 30 a health_points y elimina "power stew".

# health_points += available_items.pop("mystic bread", 0)
# # Como no existe, suma 0.

# print(available_items)
# # Imprime diccionario actualizado (sin stamina grains ni power stew).

# print(health_points)
# # Imprime 65.

# ##Get All Keys
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
# # Diccionario con estudiantes y sus calificaciones.

# print(list(test_scores))
# # Imprime solo las claves en forma de lista.

# for student in test_scores.keys():
#  print(student)
# # Itera e imprime cada clave (nombre de estudiante).

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# users = user_ids.keys()
# # Obtiene las claves (usuarios).

# lessons = num_exercises.keys()
# # Obtiene las claves (temas).

# print(users)
# print(lessons)

##Get All Values
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# for score_list in test_scores.values():
#  print(score_list)
# # Recorre e imprime todas las listas de calificaciones.

# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# total_exercises = 0
# # Inicializa acumulador.

# for exercises in num_exercises.values():
#   total_exercises += exercises
# # Suma todos los valores (ejercicios).

# print(total_exercises)
# # Imprime el total.

##Get All Items
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# for company, value in biggest_brands.items():
#  print(company + " has a value of " + str(value) + " billion dollars. ")
# # Itera claves y valores, imprime frases con las marcas.

# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# for occupation, percentage in pct_women_in_occupation.items():
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
# # Itera sobre profesiones e imprime porcentaje de mujeres en cada una.
