# Calcular el mayor de dos números ingresados por teclado usando un operador ternario

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

num_mayor = num1 if num1 > num2 else num2

print(f"El número mayor es: {num_mayor}")
