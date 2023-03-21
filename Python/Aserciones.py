def mostrar_division_entera(a, b):
    assert b >= 0 , "Ingresaron un numero negativo"
    print(a // b)

def ingresar_edad(edad):
    assert edad >= 0, "Solo se pueden ingresar edades positivas"
    assert edad >= 18, "El usuario no puede ingresar al sistema"

    return edad

# mostrar_division_entera(8,-2)

print(ingresar_edad(30))
print(ingresar_edad(17))