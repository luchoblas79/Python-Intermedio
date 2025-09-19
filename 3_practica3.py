# Determinar si un número es par o impar
def par_impar(numero):
    return f"El número {numero} es PAR." if numero % 2 == 0 else f"El número {numero} es IMPAR."


num = int(input("Ingrese un número: "))
print(par_impar(num))
