sumatorio = 0
nota_alta = 0
nota_baja = 10
contador = 0
aprobados = 0
suspensos = 0

while True:
    notas = float(input("Introduce una nota (-1 para salir): "))
    
    if notas == -1:
        break

    elif notas < -1 or notas > 10:
        print("Error. El valor introducido debe estar entre 0 y 10.")
        continue

    else:
        sumatorio += notas
        contador += 1
        
        if nota_alta < notas:
            nota_alta = notas
        
        if nota_baja > notas:
            nota_baja = notas

        if notas >= 5:
            aprobados += 1
        else:
            suspensos += 1

nota_media = sumatorio / contador

print(f"""\n-----  RESULTADOS  -----
      
Total de notas: {contador}
Nota más alta: {nota_alta}
Nota más baja: {nota_baja}
Nota media: {nota_media:.2f}

Aprobados: {aprobados} ({aprobados*100/contador:.2f}%)
Suspensos: {suspensos} ({suspensos*100/contador:.2f}%)
""")
if nota_media < 5:
    print("Grupo Mejorable")
elif nota_media >=5 and nota_media < 9:
    print("Grupo Aceptable")
else:
    print("Grupo Excelente")

print("-"*25)