def ejercicio01():
    # dados los siguientes valores
    a = 24
    b = 'coloma'
    x = [1, 2, 5, 6, 8, 9]
    y = ['manzana', 'naranjas', 'platanos', 'uva']

    # 1. mostrar una lista con los divisores de a
    for i in range(1, a + 1):
        if a % i == 0:
            print(i)

    # 2. mostrar las palabras de 'y' que su cantidad de letras es par
    for i in y:
        if len(i) % 2 == 0:
            print(i)

    # 3. mostrar la cadena b con un * entre cada letra => c*o*l*o*m*a
    '*'.join(list(b))

    # 4. filtrar los elemntos de x que son pares

    # filter con funcion standard
    def es_par(x):
        return x % 2 == 0
    list(filter(es_par, x))

    # filter con funcion lambda
    list(filter(lambda i: i % 2 == 0, x))

    # 5. mostrar los elementos de y pero solo las primeras 2 letras de cada palabra

    # for
    for i in y:
        print(i[:2])

    # map
    list(map(lambda r: r[:2], y))

    # 6. mostrar el duplicado de los elementos x => [2, 4, 10, 12, 16, 18]
    # solucion for standard
    for i in x:
        print(i * 2)

    # for python
    print([i * 2 for i in x])

    # if ternario
    print('par' if a % 2 == 0 else 'impar')
