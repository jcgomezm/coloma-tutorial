def ejemplo1():
    """
    1 hola mundo
    """
    print('hola', 'mundo')


def ejemplo2():
    """
    2 variable de tipado dinamico
    """
    x = 1
    print(x, type(x))  # tipo entero
    x = '123'
    print(x, type(x))  # tipo string
    x = 1.23
    print(x, type(x))  # tipo float
    print(x, int(x))  # redondea a entero
    x = 1
    print(float(x))  # castea a float


def ejemplo3():
    """
    3 operadores
    """
    # a = 2
    # b = 3
    # print(a + b)  # suma de enteros
    # print(a - b)  # resta de enteros
    # print(a * b)  # multiplicacion de enteros
    # print(a / b)  # division de enteros
    # a = '2'
    # b = '3'
    # print(a + b)  # concatenacion ok
    # a = 2
    # b = '3'
    # print(a + b)  # error de suma
    # a = '2'
    # b = 3
    # print(a + b)  # error de concatenacion
    a, b = 5, 2
    print(a / b)  # division exacta
    print(a // b)  # division entera
    print(a % b)  # mod o residuo


def ejemplo4():
    """
    4 strings (cadenas)
    """
    # msg = "coloma web"
    # print(msg)
    # print(msg[5])  # primera letra
    # print(msg[0:3], msg[:3])  # primeras 3 letras
    # print(msg[-1])  # última letra
    # print(msg[-6:-2])  # últimas 3 letra
    # print(msg[5:])

    # interpolacion
    a = 'coloma'
    b = 'web'
    x = 'test'
    # print('hola %s' % b)  # formato %
    # print('hola %s, soy %s' % (a, b))  # formato %
    # print('hola {}'.format(b))  # str.format()
    # print('hola {tu}, soy {yo}'.format(yo=b, tu=a))  # str.format()
    # print(f'hola {x}, soy {b}')  # f-string
    # print(f'hola {a}, soy {b} tengo { a == b } años')  # f-string

    # operadores
    a = 'Coloma'
    # print(a, len(a))
    # # print(a, 'om', a.index('om'))
    # print(a, 'om', a.count('om'))
    # print(a, a[::-1])
    # print(a, a.upper())
    # print(a, a.lower())
    x = 'Coloma WEB'
    print(x, x.split(' '))


def ejemplo5():
    """
    5 estructuras de datos
    """
    a = [1, '2', 3.0]  # lista
    # a = [1, '2', 3.0, 'A']
    # print(a)
    # print(a[-1])  # ultimo elemento
    # print(a[0])  # primer elemento
    # b = (1, '2', 3.0)  # tupla
    # print(b)

    # operaciones
    # a.append('123')  # agregar al final
    # print(a)
    # x = a.pop(0)  # quitar último
    # print(x)
    # print(a)

    # diccionarios
    c = {
        "nombre": "Jose",
        "apellido": "Gomez",
        "edad": {
            'a': 'asd',
            'b': 'das'
        }
    }
    print(c)
    print('nombre', c['edad'])


def ejemplo6():
    """
    6 condicional
    """
    # a = 3
    # b = 3
    # if a < b:
    #     print(f'{a} es menor que {b}')
    # elif a > b:
    #     print(f'{a} es mayor que {b}')
    # elif a == b:
    #     print(f'{a} es igual que {b}')
    # else:
    #     print(f'ERROR!')

    x = [1, 4, 3]
    y = 2
    if y in x:
        print(f'{y} se encuentra en {x}')

    if y not in x:
        print(f'{y} no se encuentra en {x}')
