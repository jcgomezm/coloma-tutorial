import datetime


def sin_parametros():
    print('hola mundo')


def timestamp():
    print(datetime.datetime.now())


def con_parametros(nombre, apellido):
    print(f'hola {nombre} {apellido}')


def con_pistas(cadena: str):
    print(f'es una cadena: ', cadena, type(cadena))


def con_args(*args):
    print(args)


def con_kwargs(**kwargs):
    print(kwargs)


def division_decimal(a: int, b: int) -> float:
    return a / b


def division_entera(a: int, b: int) -> (int, int):
    return (a // b), (a % b)
