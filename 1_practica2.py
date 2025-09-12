# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
A = 25
B = 0
try:
    resultado = A/B
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(resultado)
