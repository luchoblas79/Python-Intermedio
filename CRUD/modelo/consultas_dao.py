from .coneciondb import Conneccion


def crear_tabla():
    conn = Conneccion()

    sql = '''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
        CREATE TABLE IF NOT EXISTS Pais(
        ID INTEGER NOT NULL,
        Nombre TEXT,
        PRIMARY KEY (ID AUTOINCREMENT)
        );
    CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            Anio INTEGER,
            Pais INTEGER,   
            PRIMARY KEY (ID AUTOINCREMENT), 
            FOREIGN KEY (Genero) REFERENCES Genero(ID)
            );
    '''
    try:
        conn.cursor.executescript(sql)
        conn.cerrar_con()
    except:
        pass


class Peliculas():

    def __init__(self, nombre, duracion, genero, anio, pais):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.anio = anio
        self.pais = pais

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero},{self.anio},{self.pais}]'


def guardar_peli(pelicula):
    conn = Conneccion()

    sql = f'''
        INSERT INTO Peliculas(Nombre,Duracion,Genero,Anio,Pais)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},{pelicula.anio},{pelicula.pais});
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_paises():
    conn = Conneccion()
    sql = 'SELECT id, nombre FROM Pais ORDER BY nombre;'
    try:
        conn.cursor.execute(sql)
        resultados = conn.cursor.fetchall()
        conn.cerrar_con()
        return resultados
    except Exception as e:
        print(f"Error al listar países: {e}")
        return []
    
def listar_peli(condicion=None):
    conn = Conneccion()

    sql = f'''
        SELECT p.ID, p.Nombre, p.Duracion, g.Nombre, pa.Nombre, p.Anio
        FROM Peliculas as p
        INNER JOIN Genero as g
            ON p.Genero = g.ID
        INNER JOIN Pais as pa
            ON p.Pais = pa.ID  -- JOIN a la tabla Pais para obtener el nombre
        '''
    
    if condicion != None:
        sql = f'''
            SELECT p.ID, p.Nombre, p.Duracion, g.Nombre, pa.Nombre, p.Anio
            FROM Peliculas as p
            INNER JOIN Genero as g
                ON p.Genero = g.ID
            INNER JOIN Pais as pa
                ON p.Pais = pa.ID
            WHERE g.ID = {condicion};
        '''

    try:
        conn.cursor.execute(sql)
        datos = conn.cursor.fetchall()
        conn.cerrar_con()
        return datos
    except Exception as e:
        print("Error en listar_peli:", e)
        conn.cerrar_con()
        return []


def listar_generos():
    conn = Conneccion()

    sql = 'SELECT id, nombre FROM Genero ORDER BY nombre;'

    try:
        conn.cursor.execute(sql)
        resultados = conn.cursor.fetchall()
        conn.cerrar_con()

        return resultados

    except Exception as e:
        print(f"Error al listar géneros: {e}")
        return []
    finally:
        if not conn:
            conn.cerrar_con()


def editar_peli(pelicula, id):
    conn = Conneccion()

    sql = f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}, Anio ={pelicula.anio}, Pais ={pelicula.pais}
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass


def borrar_peli(id):
    conn = Conneccion()

    sql = f'''
        DELETE FROM Peliculas
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass
