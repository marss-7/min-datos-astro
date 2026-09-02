import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import seaborn as sns

df = pd.read_csv('sdss_datos.csv', skiprows=1) # SDSS incluye una línea de metadata extra
df.columns = ['class', 'z', 'dered_r']
df['distances'] = df['z'] * df['dered_r'] * 4000 # distances

print("Datos extraídos: ")
print(df.head)

# graph histogram

plt.figure(figsize=(8, 6))
plt.hist(df['distances'], bins=20, color='purple', alpha=0.7)
plt.title("Distancias")
plt.xlabel("Galaxias")
plt.show()
