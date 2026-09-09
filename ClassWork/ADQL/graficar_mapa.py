import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el CSV recién descargado
df = pd.read_csv('pleyades.csv')

plt.figure(figsize=(8,8))
plt.style.use('dark_background')
# El tamaño del punto (s) será inversamente proporcional a la magnitud (más brillante = más grande)
plt.scatter(df['RA_ICRS'], df['DE_ICRS'], s=(20-df['Gmag'])**2, color='azure', alpha=0.8)

# Convención astronómica: Invertir el eje de Ascensión Recta
plt.gca().invert_xaxis()
plt.title('Mapa Estelar: Las Pléyades (Cone Search 2 grados)')
plt.xlabel('Ascensión Recta (Grados)')
plt.ylabel('Declinación (Grados)')
plt.savefig('mapa_pleyades.png')
print("Imagen mapa_pleyades.png generada.")
