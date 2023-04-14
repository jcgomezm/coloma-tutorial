# 1. definir una clase animal y 2 clases hijas que hereden de esta

class Animal:
    def __init__(self, especie: str, nombre_comun: str):
        self.especie = especie
        self.nombre_comun = nombre_comun

class Gato(Animal):

    def __init__(self, especie: str, nombre_comun: str, nombre: str, edad: int):
        super().__init__(especie, nombre_comun)
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self, sonido):
        print(f"El {self.nombre_comun} hace {(sonido+' ')*2}")

class Perro(Animal):
    def __init__(self, especie: str, nombre_comun: str, nombre: str, raza: str ):
        super().__init__(especie, nombre_comun)
        self.nombre = nombre
        self.raza = raza

    def hacer_sonido(self,sonido):
        print(f"{self.nombre} ladra diciendo {(sonido+' ')*4}")

gato_1 = Gato('Mamifero', 'gato', 'Tom', '2')
perro_1 = Perro('mamifero','perro','Rocky','bulldog')
gato_1.hacer_sonido('miau')
perro_1.hacer_sonido('guau')

# 2. agregar metodo hacer_sonido para cada clase hija

# investigar herencia multiple en python y mixins
