# 1. definir una clase animal y 2 clases hijas que hereden de esta

class HacerSonidoMixin:

    def hacer_sonido(self, sonido):
        print('suena', sonido)


class Animal:
    especie = None
    nombre_comun = None
    nombre = None

    def __init__(self, especie: str, nombre_comun: str, nombre: str):
        self.especie = especie
        self.nombre_comun = nombre_comun
        self.nombre = nombre


class Gato(HacerSonidoMixin, Animal):
    especie = 'mamifero'
    nombre_comun = 'gato'
    edad = None

    def __init__(self, nombre: str, edad: int):
        super(Gato, self).__init__(self.especie, self.nombre_comun, nombre)
        self.edad = edad

    def hacer_sonido(self, sonido):
        super(Gato, self).hacer_sonido(sonido)
        print(f"El {self.nombre_comun} hace {(sonido + ' ') * 2}")


class Perro(Animal):
    n_vacunas = 0

    def __init__(self, especie: str, nombre_comun: str, nombre: str, raza: str):
        super().__init__(especie, nombre_comun, nombre)
        self.raza = raza

    def hacer_sonido(self, sonido):
        print(f"{self.nombre} ladra diciendo {(sonido + ' ') * 4}")

    def hacer_truco(self, truco):
        self.vacunar()
        print(f'{self.nombre} hace el truco {truco}')

    @staticmethod
    def comer():
        print('come')

    @staticmethod
    def vacunar():
        print('se vacuna')

    @classmethod
    def devolver_n_dientes(cls):
        return 40

    @classmethod
    def devolver_razas(cls):
        print('tiene', cls.n_vacunas, 'vacunas')
        cls.vacunar()
        print(cls.devolver_n_dientes())
        return ['labrador', 'pug', 'chihuahua']

# gato_1 = Gato('Tom', 2)
# gato_2 = Gato('Juan', 2)
# perro_1 = Perro('mamifero', 'perro', 'Rocky', 'bulldog')
# gato_1.hacer_sonido('miau')
# perro_1.hacer_sonido('guau')
# perro_1.hacer_truco('el muerto')
# perro_1.hacer_truco('sentado')

perro = Perro('mamifero', 'perro', 'Rocky', 'bulldog')
print(perro.hacer_truco('saltar'))

# 2. agregar metodo hacer_sonido para cada clase hija

# investigar herencia multiple en python y mixins
