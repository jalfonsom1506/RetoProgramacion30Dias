product_name = input("Nombre del producto: ").capitalize()
unit_price = float(input("Precio unitario: "))
amount = int(input("Cantidad: "))
subtotal = unit_price * amount
iva = subtotal * 0.21


print("""
-----  TICKET  -----
Producto: """, product_name, """
Cantidad: """, amount, """
Precio unitario: """, round(unit_price, 2), """€
Subtotal: """, round(subtotal, 2), """€
IVA (21%): """, round(iva, 2), """€
TOTAL: """, round(subtotal + iva, 2), """€
--------------------""")

if subtotal + iva < 20:
    print('"Compra pequeña"')
else:
    print('"Compra grande"')