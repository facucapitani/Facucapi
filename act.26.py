import math

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num2 < 0:
    
    suma_restantes = num1 + num3
    raiz_cuadrada_suma = math.sqrt(suma_restantes)
    print("La raíz cuadrada de la suma es:", raiz_cuadrada_suma)
else:
    print("Error: El segundo número no es negativo.")