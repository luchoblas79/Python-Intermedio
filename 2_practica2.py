# Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

try:
    resultado = 19 + "impar"
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(resultado)
