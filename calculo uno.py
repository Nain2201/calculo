def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Asegurarse de que el porcentaje de descuento esté en el rango correcto (0-100)
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe estar en el rango de 0 a 100")

    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento
