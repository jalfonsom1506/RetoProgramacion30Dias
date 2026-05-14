nombre = input("Introduce tu nombre: ").lower().capitalize()
nacimiento = int(input("¿En qué año naciste?: "))
ciudad = input("Indicanos tu ciudad: ").lower().capitalize()
año_actual = 2026

print("\n-----  FICHA DE USUARIO  -----")
print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")
print(f"Edad aproximada: {año_actual - nacimiento} años")
print("------------------------------\n")

if (año_actual - nacimiento) < 30:
    print("Eres joven")
else:
    print("Eres adulto")