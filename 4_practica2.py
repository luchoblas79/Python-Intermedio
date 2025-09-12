# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError,
# captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.

import os

nombre_archivo = "archivo_inexistente.txt"

try:
    with open(nombre_archivo, 'r') as f:
        contenido = f.read()
        print(f"Contenido del archivo: {contenido}")

except FileNotFoundError:

    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")

    with open(nombre_archivo, 'w') as f:
        f.write("Este es un archivo creado automáticamente porque no existía.\n")
    print(f"El archivo '{nombre_archivo}' ha sido creado.")
