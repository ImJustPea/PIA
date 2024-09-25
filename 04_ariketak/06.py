import re

# Explicación de la expresión regular:
# (?=.*[a-z])   -> Al menos una letra minúscula
# (?=.*[A-Z])   -> Al menos una letra mayúscula
# (?=.*\d)      -> Al menos un dígito
# .{8,}         -> Al menos 8 caracteres
patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

while True:
    contrasena = input("Introduce una contraseña: ")
    
    if re.match(patron, contrasena):
        print("Contraseña válida.")
        break
    else:
        print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")
