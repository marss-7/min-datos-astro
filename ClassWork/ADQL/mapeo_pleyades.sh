# !/bin/bash
# Anunciamos el inicio del proceso
echo "1. Consultando VizieR TAP mediante ADQL..."

# Guardamos la consulta pura. (Centro Pléyades: RA 56.75, Dec 24.11, Radio 2 grados)
ADQL="SELECT TOP 2000 RA_ICRS, DE_ICRS, Gmag FROM \"I/355/gaiadr3\" WHERE Gmag < 15 AND 1=CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', 56.75, 24.11, 2.0))"

# Reemplazamos los espacios por '+' usando 'sed' para que la URL no se rompa en internet
URL_ADQL=$(echo $ADQL | sed 's/ /+/g')
# Definimos el Endpoint base de VizieR
TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

# Ejecutamos wget combinando el Endpoint y la consulta codificada
wget -q -O pleyades.csv "$TAP_URL$URL_ADQL"
echo "Descarga finalizada: pleyades.csv"

echo "2. Generando script de visualización en Python..."
# Usamos el comando 'cat' para escribir un archivo de Python directamente desde la consola
cat << 'EOF' > graficar_mapa.py
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
EOF

echo "3. Ejecutando Python..."
# Ejecutamos el script que acabamos de crear
python graficar_mapa.py
