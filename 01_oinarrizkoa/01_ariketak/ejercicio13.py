x = 8
y = 12

menorQue = x < y
igualQue = x == y
multiIgual = (x * 2) == y

print("x < y?", menorQue)
print("x = y?", igualQue)
print("x * 2 = y?", multiIgual)

and_valor = igualQue and multiIgual
or_valor = igualQue or multiIgual

print("AND:", and_valor)
print("OR:", or_valor)