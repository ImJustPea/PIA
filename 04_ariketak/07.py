while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero >= 0:
            break
        else:
            print("Por favor, introduce un número entero positivo.")
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")

suma = 0
numero_user = numero 

while numero > 0:
    digito = numero % 10  # Obtener el último dígito
    suma += digito        
    numero //= 10         # Eliminar el último dígito (división entera)

print(f"La suma de los dígitos de {numero_user} es: {suma}")
