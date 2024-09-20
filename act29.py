import math

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

suma = a + b + c

if suma > 10:
    
    raiz_suma = math.sqrt(suma)
    print("La raíz cuadrada de la suma es:", raiz_suma)
else:
    
    d = int(input("Ingrese el cuarto número: "))
    e = int(input("Ingrese el quinto número: "))
    suma_total = a + b + c + d + e
    print("La suma total es:", suma_total)