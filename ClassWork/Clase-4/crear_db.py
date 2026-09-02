import sqlite3

print("=== CREADOR DE BASES DE DATOS EN PYTHON ===")
db_name = input("1. Nombre de la base de datos (ej. catalogo.db): ")
table_name = input("2. Nombre de la tabla: ")
col_cat = input("3. Nombre de columna categórica (Texto): ")
col_num = input("4. Nombre de columna numérica (Decimal): ")

# 1. Conexión a la base de datos (Crea el archivo si no existe)
conexion = sqlite3.connect(db_name)
cursor = conexion.cursor() # El cursor es el "mensajero" que envía los comandos SQL

# 2. Creación de la Tabla
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {col_cat} TEXT, {col_num} REAL)")

# 3. Ciclo para insertar múltiples registros
while True:
    print("\n-- Nuevo Registro --")
    val_cat = input(f"Ingresa {col_cat} (o escribe 'salir' para terminar): ")
    if val_cat.lower() == 'salir':
        break
    val_num = float(input(f"Ingresa {col_num}: "))
    
    # Inserción segura usando "?" para evitar "Inyecciones SQL"
    cursor.execute(f"INSERT INTO {table_name} ({col_cat}, {col_num}) VALUES (?, ?)", (val_cat, val_num))

# 4. Guardar los cambios (Commit) y cerrar
conexion.commit()
conexion.close()
print("¡Base de datos cerrada y guardada exitosamente!")
