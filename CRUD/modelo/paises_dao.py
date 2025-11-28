from .consultas_dao import listar_paises

class PaisManager:
    def __init__(self):
        self.paises = []
        self.cargar_paises()
    
    def cargar_paises(self):
        x = listar_paises()
        # Agregar una opción por defecto en el índice 0 para el Combobox
        self.paises = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for pais in x:
            self.paises.append({'id': pais[0], 'Nombre': pais[1]})
    
    def get_nombres(self):
        # Devuelve una lista de nombres para el Combobox
        return [pais['Nombre'] for pais in self.paises]
    
    def get_id_por_indice(self, index):
        # Devuelve el ID del país basado en la selección del Combobox
        if 0 <= index < len(self.paises):
            return self.paises[index]['id']
        return None
    
    def get_indice_por_nombre(self, nombre):
        # Devuelve el índice del Combobox basado en el nombre del país (para la edición)
        for i, pais in enumerate(self.paises):
            if pais['Nombre'] == nombre:
                return i
        return 0 # Devuelve 0 si no lo encuentra (Seleccione Uno)