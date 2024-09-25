user_number = int(input("Sartu zenbaki bat: "))
positive = 0
negative = 0
while user_number != 0:
    if user_number > 0:
        positive += 1
    else:
        negative += 1
    user_number = int(input("Sartu zenbaki bat: "))
    print(f"Positiboak: {positive}")
    print(f"Negatiboak: {negative}")