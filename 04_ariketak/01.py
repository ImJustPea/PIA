import random
random = random.randint(1, 100)
user_number = int(input("Sartu zenbaki bat: "))
while user_number != random:
    if user_number > random:
        print("Sartu duzun zenbakia txikiagoa da.")
    else:
        print("Sartu duzun zenbakia handiagoa da.")
    user_number = int(input("Sartu zenbaki bat: "))
print("Zorionak! Asmatu duzu zenbakia.")