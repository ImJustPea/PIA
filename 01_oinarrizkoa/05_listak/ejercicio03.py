numeros = [3, 1, 4, 5, 9, 12, 5]

print(numeros)
numeroUser = int(input("Di un numero que aparece en la lista:" ))

if numeroUser not in numeros:
    print("El numero no está en la lista")
else:
    print(numeros.count(numeroUser))