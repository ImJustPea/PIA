palabras = ["apple", "banana", "avocado", "cherry", "apricot"]
letra = 'a'
contador = 0

for palabra in palabras:
    if palabra.startswith(letra):
        contador += 1

print(letra, "->", contador)
