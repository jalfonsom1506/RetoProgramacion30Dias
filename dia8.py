import random

coche1 = input("Introduce el nombre del coche 1: ").capitalize()
coche2 = input("Introduce el nombre del coche 2: ").capitalize()
tiempos_coche1 = 0
tiempos_coche2 = 0
victorias_coche1 = 0
victorias_coche2 = 0
vuelta_rapida = 41
coche_vuelta_rapida = ""

for i in range(1, 6):
    vuelta = i
    t1 = random.randint(20, 40)
    t2 = random.randint(20, 40)
    
    

    print(f"""\n----- VUELTA {vuelta} -----

{coche1} -> {t1} segundos
{coche2} -> {t2} segundos\n""")

    if t1 % 7 == 0:
        t1 += 5
        print(f"""¡Derrape de {coche1}!
Penalización: +5 segundos
Tiempo final de la vuelta: {t1} segundos\n""")
    elif t1 % 11 == 0:
        t1 += 10
        print(f"""¡Entrada en boxes de {coche1}!
Penalización: +10 segundos
Tiempo final de la vuelta: {t1} segundos\n""")
        
    if t2 % 7 == 0:
        t2 += 5
        print(f"""¡Derrape de {coche2}!
Penalización: +5 segundos
Tiempo final de la vuelta: {t2} segundos\n""")
    elif t2 % 11 == 0:
        t2 += 10
        print(f"""¡Entrada en boxes de {coche2}!
Penalización: +10 segundos
Tiempo final de la vuelta: {t2} segundos\n""")

    tiempos_coche1 += t1
    tiempos_coche2 += t2

    if t1 < t2:
        victorias_coche1 += 1
        print(f"{coche1} ha sido más rápido en esta vuelta.\n")
    elif t2 < t1:
        victorias_coche2 += 1
        print(f"{coche2} ha sido más rápido en esta vuelta.\n")
    else:
        print(f"La vuelta ha terminado en EMPATE\n")

    if t1 < vuelta_rapida:
        vuelta_rapida = t1
        coche_vuelta_rapida = coche1
    
    if t2 < vuelta_rapida:
        vuelta_rapida = t2
        coche_vuelta_rapida = coche2

print(f"""----- RESULTADO FINAL -----
      
Tiempo total {coche1}: {tiempos_coche1} segundos
Victorias: {victorias_coche1}

Tiempo total {coche2}: {tiempos_coche2} segundos
Victorias: {victorias_coche2}

La vuelta más rápida ha sido de {coche_vuelta_rapida}
con {vuelta_rapida} segundos\n""")

if tiempos_coche1 > tiempos_coche2:
    print(f"GANADOR: {coche2}")
elif tiempos_coche2 > tiempos_coche1:
    print(f"GANADOR: {coche1}")
else:
    print("RESULTADO FINAL: EMPATE")