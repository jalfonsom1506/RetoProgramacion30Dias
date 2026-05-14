password = "Python2026"
contador = 0

registro = input("Introduce la contraseña: ")

while registro != password and contador<=3:
    contador += 1
    if contador == 1:
        print("\nInténtalo de nuevo")
        registro = input("\nIntroduce la contraseña: ")
    elif contador == 2:
        print("\nÚltimo intento")
        registro = input("\nIntroduce la contraseña: ")
    else:
        print("\n----- Cuenta bloqueada -----\n")
        break

if registro == password:        
      print(f"""
----- Acceso concedido -----
-- Bienvenido al sistema ---
\nHas necesitado {contador + 1} intentos""")