while True:

    print("""\n----- GENERADOR DE PATRONES -----

1. Rectángulo
2. Triángulo normal
3. Triángulo invertido
4. Salir""")
    
    seleccion = int(input("\nElige una opción: "))

    if seleccion < 1 or seleccion > 4:
        print("Número incorrecto. Elija una de las opciones indicadas: ")

    elif seleccion == 1:
        try:
            filas = int(input("Introduce el número de filas: "))
            columnas = int(input("Introduce el número de columnas: "))
            for rectangulo in range(filas):
                print("*" * columnas)
        except ValueError:
            print("Error. Debes introducir un número entero.")
    
    elif seleccion == 2:
        try:
            altura = int(input("Introduce la altura: "))
            for triangulo_creciente in range(altura):
                print("*" * (triangulo_creciente+1))
        except ValueError:
            print("Error. Debes introducir un número entero.")

    elif seleccion == 3:
        try:
            altura = int(input("Introduce la altura: "))
            for triangulo_invertido in range(altura):
                print(("*" * (altura - triangulo_invertido)))
        except ValueError:
            print("Error. Debes introducir un número entero")

    elif seleccion == 4:
        print("¡Gracias!")
        break