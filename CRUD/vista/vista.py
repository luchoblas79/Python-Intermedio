import tkinter as tk
from tkinter import ttk, messagebox
import modelo.consultas_dao as consulta
import modelo.generos_dao as genero
import modelo.paises_dao as pais # Importado para Pais Combobox

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=640)
        self.root = root
        self.pack()
        self.id_peli = None
        self.fondo = "#EFF383"
        self.config(bg=self.fondo) 

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        # Fila 0
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(
            font=('Arial', 12, 'bold'), bg="#FBFCDD", fg="#1931E8")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        # Fila 1
        self.label_dura = tk.Label(self, text="Duración: ")
        self.label_dura.config(
            font=('Arial', 12, 'bold'), bg="#FBFCDD", fg="#1931E8")
        self.label_dura.grid(row=1, column=0, padx=10, pady=10)

        # Fila 2
        self.label_genero = tk.Label(self, text="Genero: ")
        self.label_genero.config(
            font=('Arial', 12, 'bold'), bg="#FBFCDD", fg="#1931E8")
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Fila 3
        self.label_pais = tk.Label(self, text="Pais: ")
        self.label_pais.config(
            font=('Arial', 12, 'bold'), bg="#FBFCDD", fg="#1931E8")
        self.label_pais.grid(row=3, column=0, padx=10, pady=10)

        # Fila 4
        self.label_anio = tk.Label(self, text="Anio: ")
        self.label_anio.config(
            font=('Arial', 12, 'bold'), bg="#FBFCDD", fg="#1931E8")
        self.label_anio.grid(row=4, column=0, padx=10, pady=10)

    def input_form(self):
        # Fila 0
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled')
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Fila 1
        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)
        self.entry_duracion.config(width=50, state='disabled')
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10)

        # Fila 2 (Género Combobox)
        self.genero_manager = genero.GeneroManager()
        self.genero = tk.StringVar()
        self.entry_genero = ttk.Combobox(self, state="readonly", textvariable=self.genero)
        self.entry_genero.config(width=25, state='disabled')
        self.entry_genero['values'] = self.genero_manager.get_nombres()
        self.entry_genero.current(0)
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)

        # Fila 3 (País Combobox)
        self.pais_manager = pais.PaisManager()
        self.pais = tk.StringVar()
        self.entry_pais = ttk.Combobox(self, state="readonly", textvariable=self.pais)
        self.entry_pais.config(width=25, state='disabled')
        self.entry_pais['values'] = self.pais_manager.get_nombres()
        self.entry_pais.current(0)
        self.entry_pais.grid(row=3, column=1, padx=10, pady=10)

        # Fila 4
        self.anio = tk.StringVar()
        self.entry_anio = tk.Entry(self, textvariable=self.anio)
        self.entry_anio.config(width=50, state='disabled')
        self.entry_anio.grid(row=4, column=1, padx=10, pady=10)

    # Botones principales ahora en la FILA 5
    def botones_principales(self):
        self.btn_alta = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                             cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10) # Cambiado de row=3

        self.btn_modi = tk.Button(
            self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83',
                             cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10) # Cambiado de row=3

        self.btn_cance = tk.Button(
            self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                              cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10) # Cambiado de row=3

    # Tabla ahora en la FILA 6
    def mostrar_tabla(self):

        self.lista_p = consulta.listar_peli()

        self.lista_p.reverse()

        self.tabla = ttk.Treeview(
            self, columns=('Nombre', 'Duracion', 'Genero', 'Pais', 'Anio'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse') # Cambiado de row=4

        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse') # Cambiado de row=4
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duracion')
        self.tabla.heading('#3', text='Genero')
        self.tabla.heading('#4', text='Pais')
        self.tabla.heading('#5', text='Anio')

        for p in self.lista_p:
            self.tabla.insert('', 0, text=p[0],
                              values=(p[1], p[2], p[3], p[4], p[5]))

        # Botones de la tabla ahora en la FILA 7
        self.btn_editar = tk.Button(
            self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                               cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10) # Cambiado de row=5

        self.btn_delete = tk.Button(
            self, text='Delete', command=self.eliminar_regristro)
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                               cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10) # Cambiado de row=5

    def editar_registro(self):
        try:
            # Obtener datos de la fila seleccionada
            item = self.tabla.item(self.tabla.selection())
            self.id_peli = item['text']
            
            # Los valores de la tabla ya vienen con los nombres de Género y País
            values = item['values']
            self.nombre_peli = values[0]            
            self.dura_peli = values[1]
            self.gene_peli = values[2] # Nombre del Género
            self.pais_peli = values[3] # Nombre del País
            self.anio_peli = values[4]    

            self.habilitar_campos()
            
            # Establecer los valores en los widgets
            self.nombre.set(self.nombre_peli)   
            self.duracion.set(self.dura_peli)  
            self.anio.set(self.anio_peli)
            
            # Establecer el valor y el índice correcto para Género
            self.genero.set(self.gene_peli) 
            indice_genero = self.genero_manager.get_indice_por_nombre(self.gene_peli)
            self.entry_genero.current(indice_genero)

            # Establecer el valor y el índice correcto para País
            self.pais.set(self.pais_peli)
            indice_pais = self.pais_manager.get_indice_por_nombre(self.pais_peli)
            self.entry_pais.current(indice_pais)
            
        except Exception as e:
            # print(f"Error al editar registro: {e}")
            pass

    def eliminar_regristro(self):
        pass

    def guardar_campos(self):
        # Obtener ID de Género y País a partir del índice seleccionado
        genero_id = self.genero_manager.get_id_por_indice(self.entry_genero.current())
        pais_id = self.pais_manager.get_id_por_indice(self.entry_pais.current())

        pelicula = consulta.Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            genero_id, # Usamos el ID
            int(self.anio.get()),
            pais_id # Usamos el ID
        )

        if self.id_peli == None:
            consulta.guardar_peli(pelicula)
        else:
            consulta.editar_peli(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='readonly')
        self.entry_pais.config(state='readonly')
        self.entry_anio.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_pais.config(state='disabled')
        self.entry_anio.config(state='disabled')
        self.pais.set('') 
        self.anio.set('')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.duracion.set('')
        
        # Restablecer Combobox a la opción por defecto (índice 0)
        self.entry_genero.current(0)
        self.entry_pais.current(0)
        self.id_peli = None