import sqlite3

def conectar_db():
    return sqlite3.connect("gestion.db")

def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )               
    """)
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_id INTEGER,
            cantidad INTEGER,
            total REAL,
            fecha TEXT,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_id INTEGER,
            cantidad INTEGER,
            total REAL,
            fecha TEXT,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()