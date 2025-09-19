# Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def buscar_palabra(palabra, *args):
    return f"La palabra '{palabra}' está en la lista." if palabra in args else f"La palabra '{palabra}' NO está en la lista."


lista = input("Ingrese palabras separadas por espacio: ").split()

palabra = input("Ingrese la palabra a buscar: ")

print(buscar_palabra(palabra, *lista))
