# Calcular el promedio de una lista de números usando args y un operador ternario

def promedio(*args):
    # ternario para evitar división por cero
    return sum(args)/len(args) if args else 0


numeros = input("Ingrese los números separados por espacio: ").split()

numeros = [int(n) for n in numeros]

print("El promedio es:", promedio(*numeros))
