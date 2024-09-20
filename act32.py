sueldo_basico = float(input("Ingrese el sueldo básico: "))
categoria = int(input("Ingrese la categoría del empleado: "))

if categoria == 1:
    descuento = 0.30
elif categoria == 2 or categoria == 3:
    descuento = 0.25
elif categoria == 4:
    descuento = 0.10
else:
    descuento = 0.0

sueldo_neto = sueldo_basico - (sueldo_basico * descuento)

print("El sueldo neto es:", sueldo_neto)
print("La categoría es:", categoria)