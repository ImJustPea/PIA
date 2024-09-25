import random

random_number = random.randint(1, 50)

user_number = int(input("Un número de 1-50: "))

while user_number != random_number:
    if user_number < random_number:
        print("El número es mayor")
    else:
        print("El número es menor")
    user_number = int(input("Un número de 1-50: "))

print(f"Has acertado, el numero es {random_number}")