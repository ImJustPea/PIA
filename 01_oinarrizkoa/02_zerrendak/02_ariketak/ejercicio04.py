palabras = ["Python", "es", "un", "lenguaje", "de", "programación", "versátil"]

palabras.sort()
print(palabras)

palabrasPlus5 = sum(1 for palabra in palabras if len(palabra) > 5)
print(palabrasPlus5)

palabrasMayus = [palabra.upper() for palabra in palabras]
print(palabrasMayus)

isPython = "Python" in palabras
print(isPython)