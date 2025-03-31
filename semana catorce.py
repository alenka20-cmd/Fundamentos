def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a una compra.

    :parametro monto_total: Total de la compra.
    :parametro porcentaje_descuento: Porcentaje de descuento a aplicar 15%
    :return: Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Ejemplo de aplicacion
monto1 = 500
monto2 = 250
descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, 15)

# Cálculo del monto final
total1 = monto1 - descuento1
total2 = monto2 - descuento2

# Print resultados
print(f"Compra de ${monto1}: Descuento de ${descuento1}, Total a pagar: ${total1}")
print(f"Compra de ${monto2} con 15% de descuento: Descuento de ${descuento2}, Total a pagar: ${total2}")
