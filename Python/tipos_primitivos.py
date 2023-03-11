print('Esto es un string')
print("Esto tambien es un string \n pero con comillas dobles")

print("""

    Esto es un string multilinea.
    Muy comunmente usado para los docstrings.
    y tambien para usarlos como comentarios de bloque.

""")

enteros = 1234

print(1.1 + 2.2)

lista = [7,8,9] # Mutables
tupla = (3,4,5) # Inmutables

diccionario = { # Pares clave-valor mutables y no ordenados. Tampoco tiene repetidos.
    'nombre': 'Carlos',
    'edad': 25
}

print(diccionario['nombre'])


guia_telefonica = {
    12345678: 'Pedro',
    30303456: 'Micaela'
}

conjunto = { # Coleccion no ordenada de valores únicos MUTABLE.
    'Pera', 'Manzana', 'Uva', 'Pera', 123, True, None
}

print(conjunto)

for elemento in conjunto:
    print(elemento)

nada = None