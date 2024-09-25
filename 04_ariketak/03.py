print("1. Suma dos números")
print("2. Resta dos números")
print("3. Salir")

user_number = int(input("Selecciona una opción: "))

while user_number != 3:
    if user_number == 1:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        print(f"La suma de los dos números es: {num1 + num2}")
    elif user_number == 2:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        print(f"La resta de los dos números es: {num1 - num2}")
    else:
        print("Opción no válida")
    user_number = int(input("Selecciona una opción: "))