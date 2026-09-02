QUERY="SELECT%20TOP%2020000%20class,z,dered_r%20FROM%20SpecPhotoAll%20WHERE%20class='QSO'%20OR%20class='GALAXY'"
URL="http://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?format=csv&cmd=${QUERY}"
wget --no-check-certificate -O sdss_datos.csv "$URL"
echo "Datos de SDSS descargados."
