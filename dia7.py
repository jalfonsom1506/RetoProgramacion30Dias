productos = []
precios = []
total = 0
descuento_aplicado = False

while True:

    seleccion = int(input("""\n----- SUPERMERCADO -----
      
1. Añadir producto
2. Ver total actual
3. Aplicar descuento
4. Finalizar compra
5. Vaciar carrito

Seleccione una opción: """))
    
    if seleccion == 1:
        producto = input("Introduzca el nombre del producto: ").capitalize()
        precio = float(input("Indique su precio: "))
        print(f"Producto añadido.\n")
        productos.append(producto)
        precios.append(precio)
        total += precio

    elif seleccion == 2:
        print(f"Tienes {len(productos)} artículos añadidos")
        print(f"El importe acumulado es de {total:.2f}€")
    
    elif seleccion == 3:

        if total <= 50:
            print("No hay descuento disponible (mínimo 50€).")
    
        elif total <=100: 
            
            if descuento_aplicado == False:
                total *= 0.9
                descuento_aplicado = True
                print(f"Se aplicó un 10% de descuento. Nuevo total: {total:.2f}€")
            
            else:
                print("Ya se ha aplicado un descuento a esta compra.")

        elif total > 100:
            
            if descuento_aplicado == False: 
                total = total * 0.8
                descuento_aplicado = True
                print(f"Se aplicó un 20% de descuento. Nuevo total: {total:.2f}€")
            
            else:
                print("Ya se ha aplicado un descuento a esta compra.")
 
    elif seleccion == 4:
        print("\n----- TICKET FINAL -----")
        
        for i in range (len(productos)):
            print(f"""\nProducto: {productos [i]}
Precio: {precios[i]}€

Producto añadido correctamente.""")
            
        print("-" * 20)
        print(f"\nTotal actual: {total:.2f}€")
        print("\nCompra finalizada. ¡Que pase un buen día!\n")                  

        break

    elif seleccion == 5:
        productos.clear()
        precios.clear()
        total = 0
        descuento_aplicado = False
        print("Su carrito se ha vaciado")

    else:
        print("Debe elegir una opción entre 1 y 5")