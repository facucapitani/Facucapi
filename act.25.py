def es_primo(n):
    if n < 2:
        return False
    elif n in [2, 3, 5, 7]:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        return True

num = int(input("Ingrese un número entero positivo menor que cien: "))
if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")