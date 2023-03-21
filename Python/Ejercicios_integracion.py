# Ejercicio 1
def mcd(a, b):
    """
        mcd(8,4) = 4

        8 = 2 * 2 * 2
        4 = 2 * 2
    
        mcd(13, 6) = 1
        13 = 13
        6 = 3 * 2 
    """
    while b != 0:
        aux = a
        a = b
        b = aux % b

    return a

# Ejercicio 2
def mcm(a, b):
    return a * b / mcd(a, b)

# Ejercicio 3
def frecuencias(cadena):
    diccionario = {}
    palabras = cadena.split(" ")

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1

        else:
            diccionario[palabra] = 1

    return diccionario

# Ejercicio 4
def max_frecuencia(diccionario):
    # resultado = (maxima_frecuencia, clave)
    resultado = (0, "")
    for clave, valor in diccionario.items():
        if valor > resultado[0]:
            resultado = (valor, clave)

    return resultado

# Ejercicio 5
def get_int():
    valor = ""
    while not type(valor) is int:
        try:
            print("Ingrese un numero")
            valor = int(input("> "))

        except ValueError as ve:
            print("Por favor ingrese un numero valido")

    return valor

# Ejercicio 6
class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = self.get_nombre(nombre)
        self.__edad = self.get_nombre(edad)
        self.__dni = self.get_nombre(dni)

    def get_nombre(self, valor):
        #TODO implementar validacion de nombre
        return valor
    
    def get_edad(self, valor):
        #TODO implementar validacion de edad
        return valor
    
    def get_dni(self, valor):
        #TODO implementar validacion de dni
        return valor

    def mostrar(self):
        return f"Hola mi nombre es {self.__nombre} tengo {self.__edad} años y mi dni es {self.__dni}"
    
    def es_mayor_edad(self):
        return self.__edad >= 18

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
        self.__dni = valor

# Ejercicio 7
class Cuenta:
    def __init__(self, persona, cantidad=0):
        self.__persona = persona
        self.__cantidad = cantidad

    @property
    def persona(self):
        return self.__persona

    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return f"Titular de cuenta: {self.__persona.nombre} - dni: {self.__persona.dni}"

    def ingresar(self, monto):
        if monto <= 0:
            return
        
        self.__cantidad += monto

    def retirar(self, monto):
        self.__cantidad -= monto

# Ejercicio 8
class CuentaJoven(Cuenta):
    def __init__(self, persona, bonificacion, cantidad=0):
        super().__init__(persona, cantidad)
        self.__bonificacion = bonificacion

    def titular_valido(self):
        return self.persona.es_mayor_edad() and self.persona.edad <= 25

    def retirar(self, monto):
        if not self.titular_valido():
            print("El titular no puede retirar dinero")
            return
        
        super().retirar(monto)

    def mostrar(self):
        return f"Cuenta Joven -  Bonificación: {self.__bonificacion}"

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, valor):
        self.__bonificacion = valor 

# Tests
print(" ---- Ejecutando tests Ejercicio 1 ---- ")
assert mcd(8, 4) == 4, "la funcion mcd dio un valor incorrecto"
assert mcd(13, 6) == 1, "la funcion mcd dio un valor incorrecto"
assert mcd(75, 15) == 15, "la funcion mcd dio un valor incorrecto"
print(" ---- Ejercicio 1 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 2 ---- ")
assert mcm(8, 4) == 8, "la funcion mcm dio un valor incorrecto"
assert mcm(13, 6) == 78, "la funcion mcm dio un valor incorrecto"
assert mcm(75, 15) == 75, "la funcion mcm dio un valor incorrecto"
print(" ---- Ejercicio 2 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 3 ---- ")

assert frecuencias("hola como estas") == {'hola': 1, 'como': 1, 'estas': 1}, "frecuencias() - ERROR"
assert frecuencias("hola como estas hola como estas") == {'hola': 2, 'como': 2, 'estas': 2}, "frecuencias() - ERROR"
assert frecuencias("123456") == {'123456': 1}, "frecuencias() - ERROR"
assert frecuencias("Hola hola Adios adios adios adios") == {'Hola': 1, 'hola': 1, 'Adios': 1, 'adios': 3}, "frecuencias() - ERROR"

print(" ---- Ejercicio 3 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 4 ---- ")
assert max_frecuencia(frecuencias("hola como estas como")) == (2, 'como'), "max_frecuencias - ERROR"
assert max_frecuencia(frecuencias("Hola hola Adios adios adios adios")) == (3, 'adios'), "max_frecuencias - ERROR"
assert max_frecuencia(frecuencias("123456")) == (1, '123456'), "max_frecuencias - ERROR"
print(" ---- Ejercicio 4 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 5 ---- ")
# Descomentar para testear la funcion
# get_int()
print(" ---- Ejercicio 5 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 6 ---- ")
p1 = Persona("Carlos Lopez", 25, 1234)
p2 = Persona("Maria del Cerro", 17, 8765)
print(p1.nombre, p1.edad, p1.dni)
print(p1.mostrar())
print("Es mayor? ", p1.es_mayor_edad())
print("Es mayor? ", p2.es_mayor_edad())

print(" ---- Ejercicio 6 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 7 ---- ")
p3 = Persona("Roberto Gomez", 35, 9999)
p4 = Persona("Micalea Perez", 30, 1111)

c1 = Cuenta(p3)
c2 = Cuenta(p4, 1000)

print(c1.mostrar())
print(c1.cantidad)
print(c2.cantidad)

print("Movimientos de cuenta 1")
c1.ingresar(5000)
print(c1.cantidad)
c1.retirar(1500)
print(c1.cantidad)
print(" ---- Ejercicio 7 tests: OK ---- ")

print(" ---- Ejecutando tests Ejercicio 8 ---- ")

p5 = Persona("Miriam Clara", 35, 6741)
p6 = Persona("Miguel Aguero", 24, 1231)
cj1 = CuentaJoven(p5, .5, 1000)
cj2 = CuentaJoven(p6, .3)
print(cj1.titular_valido())
cj1.retirar(500)

print(cj2.titular_valido())
cj2.retirar(100)

print(cj1.mostrar())
print(cj2.mostrar())
print(" ---- Ejercicio 8 tests: OK ---- ")

print("todos los tests pasan OK")