user_number = int(input("Un número positivo: "))
factorial = 1
counter = 1

while counter <= user_number:
    factorial *= counter
    counter += 1
print(f"El factorial de {user_number} es {factorial}")