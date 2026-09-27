"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad

    def acelerar(self):
            self.__velocidad += 1

    def frenar(self):
            self.__velocidad -= 1

    def tocar_claxon(self):
            print("pi pi pi pi")

#Instanciar o crear objetos de la clase Coches
coche1 = Coches("Blanco", "VW", 220)
coche2 = Coches("Azul", "Nissan", 180)

#NO SE PUEDEN USAR LOS ATRIBUTOS POR QUE SON PRIVADOS
# print(f"El coche 1 es:{coche1._color}")
print("El claxon del coche 1 hace:")
coche1.tocar_claxon()

print("El claxon del coche 2 hace:")
coche2.tocar_claxon()

# print(f"La velocidad actual es: {coche1._velocidad}")
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()

# print(f"La velocidad al acelerar es: {coche1._velocidad}")





