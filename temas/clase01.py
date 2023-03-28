def ejemplo1():
    """
    1 hola mundo
    """
    print('hola mundo')


def ejemplo2():
    """
    2 variable de tipado dinamico
    """
    x = 1
    print(x, type(x))  # tipo entero
    # x = '123'
    # print(x, type(x))  # tipo string
    # x = 1.23
    # print(x, type(x))  # tipo float
    # print(x, int(x))  # redondea a entero
    # x = 1
    # print(float(x))  # castea a float


def ejemplo3():
    """
    3 operadores
    """
    a = 2
    b = 3
    print(a + b)  # suma de enteros
    # a = '2'
    # b = '3'
    # print(a + b)  # concatenacion
    # a, b = 5, 2
    # print(a / b)  # division exacta
    # print(a // b)  # division entera
    # print(a % b)  # mod o residuo


def ejemplo4():
    """
    4 strings (cadenas)
    """
    msg = 'coloma web'
    print(msg[0])  # primera letra
    # print(msg[0:3], msg[:3])  # primeras 3 letras
    # print(msg[-1])  # última letra
    # print(msg[-3:])  # últimas 3 letra

    # interpolacion
    # a = 'oloma'
    # b = 'web'
    # print('hola %s' % a)  # formato %
    # print('hola %s, soy %s' % (a, b))  # formato %
    # print('hola {}'.format(a))  # str.format()
    # print('hola {tu}, soy {yo}'.format(tu=a, yo=b))  # str.format()
    # print(f'hola {a}, soy {b}')  # f-string
    # print(f'hola {a}, soy {b} tengo { 20 + 10 } años')  # f-string

    # operadores
    a = 'Coloma'
    # print(a, len(a))
    # print(a, 'l', a.index('l'))
    # print(a, 'o', a.count('o'))
    # print(a, a[::-1])
    # print(a, a.upper())
    # print(a, a.lower())
    # x = 'Coloma WEB'
    # print(x, x.split(' '))


def ejemplo5():
    """
    5 estructuras de datos
    """
    a = [1, '2', 3.0]  # lista
    print(a)
    print(a[0])  # primer elemento
    # b = (1, '2', 3.0)  # tupla
    # print(b)
    # print(a[-1])  # ultimo elemento

    # operaciones
    # a.append('123')  # agregar al final
    # print(a)
    # a.pop()  # quitar último
    # print(a)

    # diccionarios
    # c = {
    #     "nombre": "Jose",
    #     "apellido": "Gomez",
    #     "edad": 30
    # }
    # print(c)
    # print('nombre', c['nombre'])


def ejemplo6():
    """
    6 condicional
    """
    a = 3
    b = 3
    if a < b:
        print(f'{a} es menor que {b}')
    elif a > b:
        print(f'{a} es mayor que {b}')
    else:
        print(f'{a} es igual que {b}')

    # x = [1, 2, 3]
    # y = 2
    # if y in x:
    #     print(f'{y} se encuentra en {x}')
    #
    # if y not in x:
    #     print(f'{y} no se encuentra en {x}')
