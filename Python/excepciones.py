class EsMenorDeEdadError(Exception):
    """
        Este error ocurre cuando se intenta ingresar un usuario al sistema 
        que tiene menos de 18 años.
    """
    pass

class NoPoseeTituloSecundario(Exception):
    """
        Este error ocurre cuando el usuario intenta darse de alta sin
        los papeles del secundario.
    """
    pass    

print("Comienza")

try:
    print("Todo marcha bien")
    # cuenta = 1 + "2"
    
    # resultado = 7 / 0

    # raise ValueError("Ocurrio un error de conversion de tipos")

    print("Ingrese su edad")
    edad = int(input("> "))

    if edad < 18:
        raise EsMenorDeEdadError("El usuario es menor de edad")

    print("Posee los papeles del titulo secundario?")
    respuesta = input("> ")
    if(respuesta == "n"):
        raise NoPoseeTituloSecundario("El usuario no posee titulo en tramite")

except TypeError as te:
    print(str(te), ": Se intentó sumar dos tipos invalidos")

except ZeroDivisionError as zde:
    print(str(zde), ": Se intentó divir por 0")

except ValueError as ve:
    print(str(ve), ": Se realizó una operación de tipos inválida.")

except EsMenorDeEdadError as mee:
    print(str(mee), "El usuario no puede ingresar al sistema")

except NoPoseeTituloSecundario as tse:
    print(str(tse), "El usuario debe presentar papeles")

except Exception as e:
    print(str(e), "Ups, ocurrió un error")

else:
    print("No ocurrió ningún error")

finally:
    print("realizando tareas de cierre con gracia")

print("Adios")