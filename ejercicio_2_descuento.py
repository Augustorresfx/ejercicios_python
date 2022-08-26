precio_heladera = int(input("Ingresar el precio de la heladera: "))

porcentaje_descuento = (10)

descuento_cantidad = (porcentaje_descuento * precio_heladera) / 100

precio_con_descuento = precio_heladera - descuento_cantidad

print("Precio heladera con 10% de descuento: " + str(precio_con_descuento))
