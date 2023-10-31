from __future__ import annotations
from abc import ABC, abstractmethod
from ejercicios.auxiliar import hipotenusa

#Definimos la clase abstracta creador
class Creator(ABC):

    #Creamos un metodo abstracto que sera implementado por las clases concretas
    @abstractmethod
    def factory_method(self):
        pass

    #Creamos un metodo que sera el que se encargue de llamar al metodo abstracto
    def perimetro(self):
        producto = self.factory_method()
        resultado = producto.operacion()
        return resultado

#Definimos las clases concretas creadoras
class CreatorTriangulo(Creator):
    def factory_method(self):
        return ProductoTriangulo()

class CreatorRectangulo(Creator):
    def factory_method(self):
        return ProductoRectangulo()
    
#Definimos la clase abstracta producto
class Poligono(ABC):

    @abstractmethod
    def operacion(self):
        pass

#Definimos las clases concretas producto
class ProductoTriangulo(Poligono):
    def __init__(self):
        self.cateto1 = 4
        self.cateto2 = 3

    def operacion(self):
        return hipotenusa(self.cateto1, self.cateto2) + self.cateto1 + self.cateto2

class ProductoRectangulo(Poligono):
    def __init__(self):
        self.lado1 = 5
        self.lado2 = 5

    def operacion(self):
        return (self.lado1 + self.lado2) * 2
    
#Definimos la funcion cliente
def client_code(creator: Creator) -> None:
    print(f"El perimetro del poligono es: {creator.perimetro()}", end="")

#Inicializamos el programa
if __name__ == "__main__":
    print("App lanzada con un triangulo:")
    client_code(CreatorTriangulo())
    print("\n")

    print("App lanzada con un rectangulo:")
    client_code(CreatorRectangulo())
    print("\n")