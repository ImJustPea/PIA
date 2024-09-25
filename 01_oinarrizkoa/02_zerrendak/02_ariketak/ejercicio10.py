lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
interseccion = []

for numero in lista1:
    if numero in lista2:
        interseccion.append(numero)

print(interseccion)