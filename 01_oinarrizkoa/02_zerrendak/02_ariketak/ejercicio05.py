numeros = [23, 1, 45, 34, 7, 8, 19, 56, 12]

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("mayor: ", mayor)
print("menor: ", menor)