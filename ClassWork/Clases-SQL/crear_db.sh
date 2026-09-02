echo "Creador base de Datos Ejercicio 1, telescopios.db"


# Ejecutamos la creación de la tabla inyectando las variables
sqlite3 telescopios.db "CREATE TABLE opticos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, diametro_m REAL);"

echo "--- ¡Estructura Creada! Ingresa el primer registro ---"

while 
do
read -p "Valor para nombre (ej. Sirio): " val1
read -p "Valor para diametro_m (ej. 1.45): " val2
sqlite3 telescopios.db "INSERT INTO opticos (nombre, diametro_m) VALUES ('${val1}', ${val2});"
done
