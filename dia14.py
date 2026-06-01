filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

for i in range(1, filas+1):
    for j in range(1, columnas+1):
        print(f"({i},{j})", end=" ")
        
    print()