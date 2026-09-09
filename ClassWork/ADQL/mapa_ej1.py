import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el CSV recién descargado
df = pd.read_csv('andromeda.csv')

plt.figure(figsize=(8,8))
# El tamaño del punto (s) será inversamente proporcional a la magnitud (más brillante = más grande)
plt.scatter(df['RA_ICRS'], df['DE_ICRS'], s=(20-df['Gmag'])**2, color='blue', alpha=0.8)

# Convención astronómica: Invertir el eje de Ascensión Recta
plt.gca().invert_xaxis()
plt.title('Mapa Estelar: Andrómeda (Cone Search 3 grados)')
plt.xlabel('Ascensión Recta (Grados)')
plt.ylabel('Declinación (Grados)')
plt.savefig('mapa_andromeda.png')
print("Imagen mapa_andromeda.png generada.")
