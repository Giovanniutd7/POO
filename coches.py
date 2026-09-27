"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares marca, color, modelo, veocidad, potencia y numero de acientos) y con los  operaciones y de acelerar y frenar, que los atributos y metodos sean publicos.
# Muestre el color de los coches
# Que las operaciones dismiyan o aumenten la velocidad segun sea el caso y hay que jugar con los metodos e imprimes la velocidad final


print("\033c")
class Coches:
    def __init__(self, color, marca, velocidad, modelo, p, plazas):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad
        self.__modelo = modelo
        self.__potencia = p
        self.__plazas = plazas

    def acelerar(self):
        self.__velocidad += 1
        print(self.__velocidad)

    def frenar(self):
        self.__velocidad -= 1

coche1 = Coches( "Blanco", "VW", "220", "2022", "150", "5") 
coche2 = Coches( "Azul", "Nissan", "180", "2020","150","6")

coche1.acelerar()
coche1.acelerar()




