# 1. crear una funcion que devuelve una lista con los divisores de un numero


def divisores(a):
    list_divisores = []
    for i in range(1, a + 1):
        if a % i == 0:
            list_divisores.append(i)
    print(f'El listado de divisores de {a} es: {list_divisores}')


a = int(input('Ingresa un número: \n'))
divisores(a)


# 2. crear una funcion que reciba n numeros y devuelva el producto de todos
def producto(*args):
    resultado = 1
    for arg in args:
        resultado= resultado * arg
    return resultado

# 3. crear una funcion que pinte el valor de todos los parametros que terminen en A
# pintar(comida='arroz', lampara='foco', color='azul')
# 'arroz'
# 'foco'

def pintar(**kwargs):
    lista_con_a = []
    for key, value in kwargs.items():
        if value[-1] == 'a':
            lista_con_a.append(value)
    print(lista_con_a)



# 4. crear una funcion que reciba n parametros y devuelva el producto del primero y el ultimo
# producto2(4, 2, 3, 1, 5) => 4 * 5 = 20

def producto_extremos(*args):
    resultado = args[0] * args [-1]
    print(f'El resultado de multiplicar {args[0]} por {args[-1]} es {resultado}')


# 5. crear una funcion que verifique que todos los parametros sean pares
# producto3(4, 2, 3, 1, 5) => False
# producto3(4, 2, 6, 8) => True

def pares(*args):
    for arg in args:
        if arg % 2 != 0:
            return False
    return True
