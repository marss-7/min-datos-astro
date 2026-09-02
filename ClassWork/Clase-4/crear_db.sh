#!/bin/bash

echo "=== CREADOR AUTOMÁTICO DE BASES DE DATOS ==="
read -p "1. Ingresa el nombre del archivo de la base de datos (sin extensión): " dbname
read -p "2. Ingresa el nombre de la nueva tabla: " tablename
read -p "3. Ingresa el nombre de la 1ra columna (Texto): " col1
read -p "4. Ingresa el nombre de la 2da columna (Decimal): " col2

# Ejecutamos la creación de la tabla inyectando las variables
sqlite3 ${dbname}.db "CREATE TABLE ${tablename} (id INTEGER PRIMARY KEY AUTOINCREMENT, ${col1} TEXT, ${col2} REAL);"

echo "--- ¡Estructura Creada! Ingresa el primer registro ---"
read -p "Valor para ${col1} (ej. Sirio): " val1
read -p "Valor para ${col2} (ej. 1.45): " val2

# Insertamos el registro
sqlite3 ${dbname}.db "INSERT INTO ${tablename} (${col1}, ${col2}) VALUES ('${val1}', ${val2});"

echo "¡Éxito! Base de datos ${dbname}.db creada y datos guardados."
