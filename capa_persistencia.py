import sqlite3

DB_NAME = "inter_local.db"

def inicializar_bd():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Tabla para almacenar datos del usuario
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario_table (
                identificacion TEXT PRIMARY KEY,
                usuario TEXT,
                nombre TEXT
            )
        ''')
        
        # Tabla para almacenar el esquema de tablas retornado por la API
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tablas_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_tabla TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")

def guardar_usuario(usuario, identificacion, nombre):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO usuario_table (identificacion, usuario, nombre)
            VALUES (?, ?, ?)
        ''', (identificacion, usuario, nombre))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al guardar usuario: {e}")

def guardar_tablas_esquema(tablas_lista):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Limpiamos antes de insertar los nuevos datos
        cursor.execute("DELETE FROM tablas_table")
        
        for tabla in tablas_lista:
            nombre_tabla = tabla.get("NombreTabla", str(tabla)) 
            cursor.execute("INSERT INTO tablas_table (nombre_tabla) VALUES (?)", (nombre_tabla,))
            
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al guardar tablas: {e}")

def obtener_usuario_local():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT usuario, identificacion, nombre FROM usuario_table LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"usuario": row[0], "identificacion": row[1], "nombre": row[2]}
    return None

def obtener_tablas_locales():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_tabla FROM tablas_table")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]


