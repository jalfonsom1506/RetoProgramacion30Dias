nombre = input("Introduce tu nombre: ").capitalize()

nota = float(input("Indícanos la nota obtenida (0 a 10): "))

while nota < 0 or nota > 10:
    print("Resultado: Nota no válida")
    nota = float(input("Indícanos la nota obtenida (0 a 10): "))

print(f"""
Alumno: {nombre}
Nota: {nota}""")
if nota < 5:
    print("Resultado: Suspenso -> Hay que seguir trabajando")
elif nota < 7:
    print("Resultado: Aprobado -> Buen trabajo")
elif nota < 9:
    print("Resultado: Notable -> Buen trabajo")
else:
    print("Resultado: Sobresaliente -> Buen trabajo")