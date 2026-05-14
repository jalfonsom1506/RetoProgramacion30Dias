try:

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    if num1 < num2:
        mayor, menor = num2, num1
    elif num1 > num2:
        mayor, menor = num1, num2
    else:
        print("Los números son iguales")
    
    print(f"""\n----- RESULTADOS -----
      
    Número mayor: {mayor}
    Número menor: {menor}

    Suma: {mayor + menor}
    Diferencia: {mayor - menor}

    Número 1: 
    - {"Positivo" if num1 > 2 else "Negativo"}
    - {"Par" if num1 % 2 == 0 else "Impar"}

    Número 2: 
    - {"Positivo" if num2 > 0 else "Negativo"}
    - {"Par" if num2 % 2 == 0 else "Impar"}
    ----------------------""")
except ValueError:
    print("Error: Introduzca sólo números enteros")