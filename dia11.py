while True:

    print("""----- GENERADOR DE PATRONES -----

1. Rectángulo
2. Triángulo normal
3. Triángulo invertido
4. Salir""")

    seleccion = int(input("Elige una opción: "))

    if seleccion < 1 or seleccion > 4:
        print("Número incorrecto. Elija una de las opciones indicadas: ")

    elif seleccion == 1:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        for rectangulo in range(filas):
            print("*" * columnas)

    elif seleccion == 2:
        altura = int(input("Introduce la altura: "))
        for triangulo_creciente in range(altura):
            print("*" * (triangulo_creciente+1))

    elif seleccion == 3:
        altura = int(input("Introduce la altura: "))
        for triangulo_invertido in range(altura):
            print(("*" * (altura - triangulo_invertido)))

    elif seleccion == 4:
        break