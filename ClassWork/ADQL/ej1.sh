# taken directly from the class 5 notebook, modified
# Guardamos la consulta pura.

ADQL="SELECT TOP 2000 RA_ICRS, DE_ICRS, Gmag FROM \"I/355/gaiadr3\" WHERE Gmag < 16 AND 1=CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', 10.68, 41.26, 3.0))"
# Reemplazamos los espacios por '+' usando 'sed' para que la URL no se rompa en internet
URL_ADQL=$(echo $ADQL | sed 's/ /+/g')
# Definimos el Endpoint base de VizieR
TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

# Ejecutamos wget combinando el Endpoint y la consulta codificada
wget -O andromeda.csv "$TAP_URL$URL_ADQL"
echo "Descarga finalizada: andromeda.csv"


echo "2. Generando script de visualización en Python..."
# Usamos el comando 'cat' para escribir un archivo de Python directamente desde la consola
cat << 'EOF' > mapa_ej1.py
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
EOF

echo "3. Ejecutando Python..."
# Ejecutamos el script que acabamos de crear
python mapa_ej1.py

