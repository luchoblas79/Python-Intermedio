# Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

diccionario = {"Nombre": "Pedro", "Apellido": "Gomez"}

clave_faltante = "Edad"
try:
    resultado = diccionario[clave_faltante]
    print(f"El valor de {clave_faltante} es: {resultado}")
except KeyError:
    print(
        f"Ha ocurrido un error. La clave {clave_faltante} no existe en el diccionario.")
