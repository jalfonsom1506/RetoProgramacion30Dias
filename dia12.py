import random

monedas = 10
simbolos = ["🍒", "🍋", "⭐", "🔔"]

while True:

    print(f"""----- TRAGAPERRAS -----

Saldo actual: {monedas} monedas
          
1. Jugar partida
2. Añadir saldo
3. Ver saldo
4. Salir""")
    
    try:
        seleccion = int(input("¡Bienvenido! Elije una opción: "))
    except ValueError:
        print("Error. Debe introducir un número. Inténtelo de nuevo: ")
        continue

    if seleccion < 1 or seleccion > 4:
        print("La opción elegida no existe. Elija una de las opciones: ")

    elif seleccion == 1:
        if monedas < 1:
            print ("No tienes saldo suficiente. Por favor, recarga")
        else:
            print(f"""¡TIRADA!. Has gastado una moneda.
¡COMBINACIÓN!: """)
            monedas -= 1
            resultado = [random.choice(simbolos) for _ in range (3)]
            
            if resultado [0] == resultado [1] == resultado [2]:
                print(f"""Tu saldo: {monedas} monedas

{resultado[0],resultado[1],resultado[2]}

🎉 ¡PREMIO MAYOR! 🎉
Has ganado 10 monedas

Saldo actual: {monedas+10} monedas """)
                monedas += 10

            elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
                print(f"""Tu saldo: {monedas} monedas

{resultado[0],resultado[1],resultado[2]}

🎉 ¡Enhorabuena! 🎉
Has ganado 3 monedas

Saldo actual: {monedas+3} monedas """)
                monedas += 3

            else: 
                print(f"""\nSaldo actual: {monedas} monedas

{resultado[0],resultado[1],resultado[2]}

No ha habido suerte... ¡Sigue jugando!\n""")
    
    elif seleccion == 2:
        try:
            ingreso = int(input("\n¿Cuántas monedas quieres añadir?: "))
            if ingreso > 0:
                monedas += ingreso
                print(f"""\nSe han añadido {ingreso} monedas a tu cuenta.

Saldo actual: {monedas} monedas\n""")
            else:
                print("Debe introducir un número positivo de, al menos, 1 moneda\n")
        except ValueError:
            print("Error. Debe introducir un número entero positivo\n")
    
    elif seleccion == 3:
        print(f"Su saldo actual es de {monedas} monedas")

    elif seleccion == 4:
        print("Gracias por su visita. ¡Le esperamos pronto!")
        break