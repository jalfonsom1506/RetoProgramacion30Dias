precio_compra = float(input("Precio de la compra: "))
while precio_compra <= 0:
        precio_compra = float(input("El precio de la compra no puede ser 0. Introduzca el precio de la compra: "))

entregado = float(input("Dinero entregado: "))
while entregado < precio_compra:
    entregado = float(input(f"El dinero entregado es inferior al importe de la compra ({precio_compra}). Introduzca una nueva cantidad: "))

cambio = ((entregado*100-precio_compra*100)/100)

print(f"\nCambio total: {cambio}€\n")

cash = [
      (50000, "Billetes de 500 euros"), (20000, "Billetes de 200 euros"),
      (10000, "Billetes de 100 euros"), (5000, "Billetes de 50 euros"),
      (2000, "Billetes de 20 euros"), (1000, "Billetes de 10 euros"),
      (500, "Billetes de 5 euros"), (200, "Monedas de 2 euros"),
      (100, "Monedas de 1 euro"), (50, "Monedas de 50 centimos"),
      (20, "Monedas de 20 centimos"), (10, "Monedas de 10 centimos"),
      (5, "Monedas de 5 centimos"), (2, "Monedas de 2 centimos"),
      (1, "Monedas de 1 centimo"), 
]

a_devolver = int(round(cambio*100))

for valor, denominacion in cash:
      if a_devolver >= valor:
            cantidad = a_devolver // valor
            a_devolver %= valor
            print(f"{denominacion}: {cantidad} ")