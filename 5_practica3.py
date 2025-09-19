# Imprimir un mensaje de error si no se pasan suficientes argumentos
def calcular_promedio(*args):
    return sum(args) / len(args) if len(args) >= 2 else None


numeros = input("Ingrese los números separados por espacio: ").split()
numeros = [int(n) for n in numeros]

resultado = calcular_promedio(*numeros)
print("El promedio es:", resultado) if resultado is not None else print(
    "Error: se necesitan al menos 2 números")
