frascos = {
    1: "chico",
    2: "mediano",
    3: "grande"
}

codigo = int(input("Ingrese el código del frasco: "))

if codigo in frascos:
    print("El frasco es:", frascos[codigo])
else:
    print("Código no válido")