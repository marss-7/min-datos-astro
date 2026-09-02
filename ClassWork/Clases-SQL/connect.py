import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import seaborn as sns

conexion = sqlite3.connect('telescopios.db')
consulta = "SELECT * FROM opticos ORDER BY id ASC;"

df = pd.read_sql_query(consulta, conexion)

conexion.close()

print("Datos extraídos: ")
print(df)

# graph !!!

plt.figure(figsize=(8,6))
sns.barplot(data=df, x=df.columns[1], y=df.columns[2], palette='magma')
plt.title('Análisis de Base de Datos SQLite via Pandas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_python_sql.png')
