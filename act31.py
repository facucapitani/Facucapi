num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 == 1:
    resultado = num2 + num3
    print("El resultado es:", resultado)
elif num1 == 2:
    resultado = num2 * num3
    print("El resultado es:", resultado)
elif num1 == 3:
    
    if num3 != 0:
        resultado = num2 / num3
        print("El resultado es:", resultado)
    else:
        print("Error: no se puede dividir entre cero")
elif num1 == 4:
    
    resultado = (num2 ** 2 + num3 ** 2) ** 0.5
    print("El resultado es:", resultado)
else:
    print("Error: código no válido")