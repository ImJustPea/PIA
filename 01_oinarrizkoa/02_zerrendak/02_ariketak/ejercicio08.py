lista = [1, 2, 3, 2, 4, 2]
numero = 2
indices = []

for i in range(len(lista)):
    if lista[i] == numero:
        indices.append(i)

print(numero, "->", indices)