# Script para concatenar los datos y guardarlos en un archivo de texto
def guardar_datos_concatenados(barrios, datos_hombres, datos_mujeres, ruta_fichero):
    # Crear las cadenas concatenadas para hombres y mujeres
    cadena_hombres = ' '.join(str(x) for x in datos_hombres)
    cadena_mujeres = ' '.join(str(x) for x in datos_mujeres)

    # Guardar en un archivo de texto
    with open(ruta_fichero, 'w') as file:
        file.write(f"Barrios: {' '.join(barrios)}\n")
        file.write(f"Hombres (De 5 a 9 años): {cadena_hombres}\n")
        file.write(f"Mujeres (De 5 a 9 años): {cadena_mujeres}\n")

    print(f"Datos concatenados guardados exitosamente en {ruta_fichero}")
