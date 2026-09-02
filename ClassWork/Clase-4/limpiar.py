import pandas as pd
import sqlite3
# Cargamos el CSV a Pandas
df = pd.read_csv('exoplanetas.csv')
# Limpieza rápida: Borramos filas sin masa o sin radio
df = df.dropna(subset=['pl_rade', 'pl_bmasse'])
# Conectamos a una base de datos local
conn = sqlite3.connect('mi_archivo_nasa.db')
# ¡Magia! Guardamos todo el DataFrame como una tabla SQL
df.to_sql('planetas', conn, if_exists='replace', index=False)
conn.close()
print('Exoplanetas migrados a mi_archivo_nasa.db exitosamente.')

