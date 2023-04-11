class Persona:
    nombre = None
    edad = None
    tiene_pulgas = True

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hello I'm {self.nombre} and I'm {self.edad} years old")

    def __str__(self):
        return self.nombre

    def correr(self):
        pass


class Profesor(Persona):
    def enseñar(self):
        print(f'Estoy enseñando...')


class Alumno(Persona):
    def estudiar(self):
        print(f'Estoy estudiando...')


class Clase:
    nombre = None
    profesor = None
    alumnos = []

    def __init__(self, nombre, profesor, alumnos):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = alumnos

    def pintar_reporte(self):
        print('nombre', self.nombre)
        print('profesor', self.profesor)
        for i in self.alumnos:
            print('alumnos', i)


class Figura:
    numero_lados = None
    tamano_lado = None

    def __init__(self, numero_lados, tamano_lado):
        self.numero_lados = numero_lados
        self.tamano_lado = tamano_lado

    def calcular_perimetro(self):
        return self.numero_lados * self.tamano_lado

    def calcular_area(self):
        return self.tamano_lado * self.tamano_lado


class Triangulo(Figura):
    altura = None

    def __init__(self, tamano_lado, altura):
        super().__init__(3, tamano_lado)
        self.altura = altura

    def calcular_area(self):
        return (self.tamano_lado * self.altura) / 2


class Cuadrado(Figura):

    def __init__(self, tamano_lado):
        super().__init__(4, tamano_lado)

    def pintar(self, *args, **kwargs):
        print('args', args)
        print('kwargs', kwargs)


class Motor:
    caballos_fuerza = None

    def __init__(self, caballos_fuerza):
        self.caballos_fuerza = caballos_fuerza

    def __str__(self):
        return f'motor de {self.caballos_fuerza} caballos de fuerza'


class Rueda:
    tamano = None

    def __init__(self, tamano):
        self.tamano = tamano

    def __str__(self):
        return f'RUEDA {self.tamano}'


class Auto:
    marca = None
    motor = None
    ruedas = []

    def __init__(self, marca, motor, n_ruedas):
        self.marca = marca
        self.motor = motor
        for i in range(0, n_ruedas):
            nueva_rueda = Rueda(50)
            self.ruedas.append(nueva_rueda)

    def pintar_reporte(self):
        print('marca', self.marca)
        print('motor', self.motor)
        for i in self.ruedas:
            print(i)


class Animal:
    tiene_pulgas = False


class AullarMixin:
    @classmethod
    def aullar(cls):
        print('auuuuuu')


class HombreLobo(Animal, Persona, AullarMixin):
    pass
