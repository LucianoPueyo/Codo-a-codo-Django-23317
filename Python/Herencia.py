class Estudiante:
    def __init__(self, carrera):
        self.__carrera = carrera
        self.__materias_aprobadas = 0

    @property
    def carrera(self):
        return self.__carrera
    
    @property
    def materias_aprobadas(self):
        return self.__materias_aprobadas
    
    def aprobar_materia(self):
        self.__materias_aprobadas += 1


class Empleado:
    def __init__(self, nombre, apellido):
        # al tener un doble guion bajo (__) los atributos
        # son privados.
        self.__nombre = nombre
        self.__apellido = apellido

    # Getters y Setters
    @property # Getter del atributo nombre
    def nombre(self):
        return self.__nombre

    @nombre.setter # Setter del atributo nombre
    def nombre(self, valor):
        self.__nombre = valor

    @property # Getter del atributo apellido
    def apellido(self):
        return self.__apellido

    @apellido.setter # Setter del atributo apellido
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def nombre_completo(self):
        return f"Hola, mi nombre es {self.__nombre} {self.__apellido}"
    
    @property
    def salario(self):
        """
        La clase padre Empleado define el metodo salario.
        Lo que no define es su implementacion.

        Por lo tanto, las clases hijas serán las responsables
        de indicar como se implementa dicho metodo.
        """
        pass


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    

class EmpleadoPorHora(Empleado, Estudiante):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora, carrera):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, carrera)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * 21 * self.__valor_hora


e1 = Empleado("Carlos", "Lopez")
print(e1.nombre, e1.apellido)

e1.nombre = "Roberto"
e1.apellido = "Gomez"

print(e1.nombre_completo)


e2 = EmpleadoFullTime("Maria", "Del Cerro", 80000)
e3 = EmpleadoPorHora("Camila","Arias", 6, 1000, "Sistemas")
print(e2.nombre_completo)
print(e2.salario)

print(e3.nombre_completo)
print(e3.salario)