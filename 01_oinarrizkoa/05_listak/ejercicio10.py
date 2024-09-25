numeros = [1, 2, 3, 4, 5, 6]

for i in range(len(numeros)):
    del numeros[len(numeros)-1]
    print(numeros)
    
#------------------------------

numeros = [1, 2, 3, 4, 5, 6]
numeros.clear()
print(f"{numeros} con clear")