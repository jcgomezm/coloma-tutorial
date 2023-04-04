import datetime


def sin_parametros():
    print('hola mundo')


def timestamp():
    print(datetime.datetime.now())


def con_parametros(nombre, apellido):
    print(f'hola {nombre} {apellido}')


def con_parametros_defecto(nombre, apellido='desconocido'):
    print(f'hola {nombre} {apellido}')


def con_pistas(cadena: str):
    print(f'es una cadena: ', cadena, type(cadena))


def con_args(*args):
    print(f'el primer parametro es {args[0]}')
    print(f'el ultimo parametro es {args[-1]}')


# keyword arguments
def con_kwargs(**kwargs):
    print(f"nombre: {kwargs['nombre']}")
    if 'apellido' in kwargs:
        print(f"apellido: {kwargs['apellido']}")


def division_decimal(a: int, b: int) -> float:
    if b == 0:
        return 'error division entre 0'
    print('continua la funcion')
    return a / b


def division_entera(a: int, b: int) -> (int, int):
    return (a // b), (a % b)
