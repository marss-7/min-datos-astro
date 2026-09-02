import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Establecemos conexión con el archivo creado previamente por la consola (o por el script)
conexion = sqlite3.connect('cositas.db')

# 2. Definimos nuestra consulta SQL
# NOTA: Debes reemplazar 'mi_tabla' por el nombre que le diste al crearla
consulta = "SELECT * FROM phoebe ORDER BY id ASC;"

# 3. Pandas ejecuta la consulta y convierte el resultado en DataFrame al instantdf = pd.read_sql_query(consulta, 
df = pd.read_sql_query(consulta, conexion)

# 4. Cerramos conexión por seguridad
conexion.close()

# Mostramos los datos en la terminal
print("Datos extraídos de la Base de Datos:")
print(df)

# 5. Visualizamos los datos (Asumiendo que col_cat y col_num son las variables que ingresamos)
plt.figure(figsize=(8,6))
sns.barplot(data=df, x=df.columns[1], y=df.columns[2], palette='seismic')
plt.title('Análisis de Base de Datos SQLite via Pandas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_python_sql.png')
