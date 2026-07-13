import sqlite3
from pathlib import Path

# Aquí defino la ruta de la base de datos usando pathlib porque el sistema operativo donde desarrollo es macOS
# y la calificacion seguramente será realizada en windows, me evito problemas de esta manera.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "productos.db"

def obtener_conexion():
    try:
        conexion = sqlite3.connect(DB_PATH)
        conexion.execute("PRAGMA foreign_keys = ON;")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def inicializar_base_datos():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL
                );
            """)
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            conexion.close()

#              ****OPERACIONES CRUD****

def crear_producto(nombre: str, precio: float, stock: int) -> bool:
    conexion = obtener_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?);"
        cursor.execute(query, (nombre, precio, stock))
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al insertar producto: {e}")
        return False
    finally:
        conexion.close()

def leer_productos() -> list:
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor()
        query = "SELECT id, nombre, precio, stock FROM productos ORDER BY id DESC;"
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al consultar productos: {e}")
        return []
    finally:
        conexion.close()

def actualizar_producto(id_producto: int, nombre: str, precio: float, stock: int) -> bool:
    conexion = obtener_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        query = """
            UPDATE productos 
            SET nombre = ?, precio = ?, stock = ? 
            WHERE id = ?;
        """
        cursor.execute(query, (nombre, precio, stock, id_producto))
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al actualizar producto: {e}")
        return False
    finally:
        conexion.close()

def eliminar_producto(id_producto: int) -> bool:
    conexion = obtener_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = ?;"
        cursor.execute(query, (id_producto,))
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al eliminar producto: {e}")
        return False
    finally:
        conexion.close()