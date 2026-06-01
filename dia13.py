import random

def elegirNivel():
    oxigeno = 0
    comida = 0
    energia = 0

    while True:
        nivel = int(input("""Elija el nivel de su juego: 

1 - FÁCIL
2 - INTERMEDIO
3 - DIFÍCIL
> """))

        match nivel:
            case 1:
                oxigeno += 120
                comida += 100
                energia += 80
                break
            
            case 2:
                oxigeno += 100
                comida += 80
                energia += 60
                break

            case 3:
                oxigeno += 80
                comida += 60
                energia += 40
                break

            case _:
                print("\n[Error] Opción no válida. Por favor, vuelva a elegir.\n")
                

    print(f"""Recursos asignados con éxito:
          
Oxígeno: {oxigeno} | Comida: {comida} | Energía: {energia}""")

    return oxigeno, comida, energia

def accionDiaria(oxigeno, comida, energia, dia):

    while True:

        accion = int(input(f"""----- DÍA {dia} -----
                    
Elija una acción a realizar: 
1. Buscar comida
2. Reparar sistema de oxígeno
3. Descansar"""))
                
        match (accion):
            case 1:
                comida += 20
                oxigeno -= 5
                energia -= 15
                print(f"""--- Has encontrado suministros de comida ---
                        
Recursos:
                    
Comida: {comida}
Oxígeno: {oxigeno}
Energía: {energia}""")
                break

            case 2:
                comida -= 5
                oxigeno += 10
                energia -= 20
                print(f"""--- Has reparado parte del sistema de oxígeno ---
                        
Recursos:
                    
Comida: {comida}
Oxígeno: {oxigeno}
Energía: {energia}""")
                break

            case 3:
                comida -= 10
                oxigeno -= 5
                energia += 15
                print(f"""--- Has descansado y recuperado energía ---
                        
Recursos:
                    
Comida: {comida}
Oxígeno: {oxigeno}
Energía: {energia}""")
                break

            case _:
                print(f"Selección no válida. Elija una acción: ")
                    
    return oxigeno, comida, energia



def eventoAleatorio(oxigeno, comida, energia):

    print("---------- REGISTRO DIARIO DE INCIDENCIAS ----------")

    opciones = [1, 2, 3, 4]

    num_aleatorio = random.choice(opciones)

    match num_aleatorio:
        case 1: 
            oxigeno -= 15
            print(f"""¡Atención! Ha habido una fuga de oxígeno.

Oxígeno: {oxigeno}""")        
            
        case 2: 
            energia += 10
            print(f"""¡Atención! Se han activado los paneles solares.
                    
Energia: {energia}""")
    
        case 3: 
            comida += 15
            print(f"""¡Enhorabuena! Has encontrado suministros extra.
                    
Comida: {comida}""")
            
        case 4: print("Hoy no se ha registrado ningún incidente")

    return oxigeno, comida, energia

print("""------------------------------------------------------------------
FROM: NASA
TO: COMANDANTE DE ORION-GH317
PRIORITY: HIGH

Tu nave espacial se ha averiado
El equipo de rescate está en camino
El tiempo hasta su llegada es de 7 días
Debes sobrevivir en territorio hostil hasta su llegada
Todo nuestro personal está trabajando en su rescate
Estamos seguro de su capacidad para el éxito de la misión
Saludos desde la tierra. ¡Suerte!
------------------------------------------------------------""")
        
oxigeno_juego, comida_juego, energia_juego = elegirNivel()

for dia in range (1, 8):
    oxigeno_juego, comida_juego, energia_juego = accionDiaria(oxigeno_juego, comida_juego, energia_juego, dia)

    oxigeno_juego, comida_juego, energia_juego = eventoAleatorio(oxigeno_juego, comida_juego, energia_juego)

    if oxigeno_juego <= 0 or energia_juego <= 0 or comida_juego <= 0:
        print("""\n==============================================
¡MISIÓN FALLIDA! Te has quedado sin recursos vitales en el espacio.
==============================================""")
        break

else:
        print("""\n==============================================
    ¡ENHORABUENA COMANDANTE! El equipo de rescate ha llegado.
    Has sobrevivido a la misión ORION-GH317 con éxito.
    ==============================================""")