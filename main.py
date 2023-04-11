from temas.clase03 import Alumno, Profesor, Clase, Triangulo, Cuadrado, Auto, Motor, HombreLobo


def runPersona():
    alumno = Alumno('Guille', 30)
    profesor = Profesor('Luis', 29)

    alumno.saludar()
    alumno.estudiar()
    profesor.saludar()
    profesor.enseñar()

    clase = Clase('Python', profesor, [alumno])
    clase.pintar_reporte()

    # hombre_lobo = HombreLobo(nombre='Mike', edad=20)
    # hombre_lobo.saludar()
    # hombre_lobo.aullar()

    HombreLobo.aullar()


def runFigura():
    triangulo = Triangulo(tamano_lado=5, altura=10)
    print(triangulo.calcular_perimetro())
    print(triangulo.calcular_area())

    cuadrado = Cuadrado(tamano_lado=5)
    print(cuadrado.calcular_perimetro())
    print(cuadrado.calcular_area())

    l = [triangulo, cuadrado]
    for i in l:
        print('for', i.calcular_area())


def runAuto():
    motor = Motor(500)
    auto = Auto('Toyota', motor, 4)
    auto.pintar_reporte()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runPersona()
