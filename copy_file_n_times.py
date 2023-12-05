import shutil
import os
import sys

def copiar_archivo(origen, destino):
    shutil.copy(origen, destino)
# Ruta del archivo que deseas copiar

if len(sys.argv) < 3:
    print("Por favor, proporciona como argumento:")
    print("1.- Nombre del archivo que desea copiar")
    print("2.- Numero de veces que desea copiar el archivo")
    print("Ejemplo: ")
    print("python3 import.py archivo.pdf 10")
    sys.exit(1)

archivo_a_copiar = sys.argv[1]
veces_a_copiar = int(sys.argv[2])
# Directorio donde se copiarán los archivos
directorio_destino = 'destino/'
# Crear el directorio de destino si no existe
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)
# Copiar el archivo 100 veces
for i in range(1, veces_a_copiar + 1):
    nombre_archivo_copia = f'{archivo_a_copiar[:-4]}_{i}.pdf'
    ruta_destino = os.path.join(directorio_destino, nombre_archivo_copia)
    copiar_archivo(archivo_a_copiar, ruta_destino)
print(f'Se han copiado {i} veces el archivo "{archivo_a_copiar}" en el directorio "{directorio_destino}".')

