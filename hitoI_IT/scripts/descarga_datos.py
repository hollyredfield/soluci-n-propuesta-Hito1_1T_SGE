# Script para descargar el archivo Excel
import os
import requests


# Función para descargar el archivo

def descargar_archivo(url, ruta_archivo):
    # crear la carpeta 'data' si no existe
    directorio = os.path.dirname(ruta_archivo)
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # descargar el archivo

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # status_code == 200 significa solicitud existosa
        with open(ruta_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Descarga completada: {ruta_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")

