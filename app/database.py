
import sqlite3

connection = sqlite3.connect("dbdreams.db")
connection.row_factory = sqlite3.Row

CREA_TABLA = """CREATE TABLE IF NOT EXISTS dreams (
    dream TEXT,
    fecha TEXT
);
"""

INSERTA_DREAMS = """INSERT INTO dreams VALUES (?,?);"""

LISTA_DREAMS = """SELECT * FROM dreams;"""

BUSCAR = """SELECT * FROM dreams WHERE dream LIKE ?;"""

BUSCAR_DATE = """ SELECT * FROM dreams WHERE fecha LIKE ?,"""

def create_tables():
    with connection: 
        connection.execute(CREA_TABLA)


def add_dream(contenido,fecha):
    with connection:
       #ataques de inyeccion"
       #connection.execute(f"INSERT INTO dreams VALUES ('{contenido}', '{fecha}')") 
        ## forma correcta
        connection.execute(INSERTA_DREAMS, (contenido, fecha))

def get_dreams():
    cursor = connection.cursor()
    cursor.execute(LISTA_DREAMS)
    return cursor

def buscar_dream_por_palabra(palabra_clave):
    cursor  = connection.cursor()
    cursor.execute(BUSCAR, (f"%{palabra_clave}%",)) 
    return cursor

def buscar_dream_por_fecha(fecha_clave):
    cursor = connection.cursor()
    cursor.execute(BUSCAR_DATE, (f"%{fecha_clave}",))

def close_connection():
    connection.close()






