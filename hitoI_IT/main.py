# Script principal que ejecuta todo el flujo del ejercicio


# URL de archivo seleccionado (Ayto Madrid_)
# Distritos en cifras (información de Barrios) 
# Retiro_Población por Edad y Sexo

import pandas as pd

from scripts.descarga_datos import descargar_archivo
from scripts.limpieza_datos import cargar_dataset, eliminar_filas, eliminar_primera_columna, reemplazar_nan, verificar_datos_inconsistentes
from scripts.transformacion_datos import TransformarDatos
from scripts.guardar_datos import guardar_datos_concatenados
from scripts.estadisticas_poblacion import EstadisticasPoblacion
from scripts.poblacion_barrio import PoblacionBarrio

# Ruta del archivo y nombre
url = 'https://www.madrid.es/UnidadesDescentralizadas/UDCEstadistica/Nuevaweb/Distritos/Distritos%20en%20cifras%20barrios/03%20-%20Retiro/D03T0323.xlsx'
ruta_archivo = 'data/Retiro_Poblacion por Edad y Sexo.xlsx'

# Descarga de archivo
descargar_archivo(url, ruta_archivo)

# Cargar dataframe y limpiar datos
df = cargar_dataset(ruta_archivo)
filas_a_eliminar = [0, 1, 2, 3, 6, 8, 31, 33, 56, 58, 81]
df = eliminar_filas(df, filas_a_eliminar)
df = eliminar_primera_columna(df)
df = reemplazar_nan(df)

# Validar datos inconsistentes

df = verificar_datos_inconsistentes(df)

# Verificar si quedan valores NaN
print(df.isnull().sum())

# Mostrar el dataframe limpio
print(df.head(25))

# Trasponer filas por columnas
# Creamos el objeto TransformarDatos
transformador = TransformarDatos(df)
df_transformado = transformador.cambiar_filas_por_columnas()

# Ajustar el índice ignorando la primera columna "Unnamed"
df_transformado = transformador.ajustar_indice()

# Extraer los datos de la categoría "De 5 a 9 años" para hombres (columna E) y mujeres (columna AB) en los barrios (índices 3-8)
# Columna AB para hombres (index 25) y columna Ay para mujeres (index 48)
# Barrios (índices 3-8)
datos_hombres, datos_mujeres = transformador.extraer_datos_por_rango_edad(25, 48, 2, 8)

# Renombrar las series de datos
datos_hombres.name = "De 5 a 9 años - Hombres"
datos_mujeres.name = "De 5 a 9 años - Mujeres"

# Convertir a tipo numérico si es necesario (para evitar problemas con estadísticas)
datos_hombres = pd.to_numeric(datos_hombres, errors='coerce')
datos_mujeres = pd.to_numeric(datos_mujeres, errors='coerce')

# Mostrar el dataframe transformado (traspuesto)
print(df_transformado.head(25))

# Mostrar los resultados de hombres y mujeres por barrio
print("Datos de hombres (De 5 a 9 años) por barrio:")
print(datos_hombres)

print("Datos de mujeres (De 5 a 9 años) por barrio:")
print(datos_mujeres)

# Extraer los nombres de los barrios
barrios = datos_hombres.index.tolist()  # Asumimos que el índice contiene los nombres de los barrios

# Crear el objeto EstadisticasPoblacion
estadisticas = EstadisticasPoblacion(datos_hombres, datos_mujeres, barrios)

# Calcular estadísticas
media_hombres_porBarrio, media_mujeres_porBarrio = estadisticas.calcular_media()
varianza_hombres_porBarrio, varianza_mujeres_porBarrio = estadisticas.calcular_varianza()
moda_hombres_porBarrio, moda_mujeres_porBarrio = estadisticas.calcular_moda()

#Guardar el dataframe transformado como Excel
df_transformado.to_excel('data/df_transformado.xlsx', index=True)  # 'index=True' para incluir el índice

# Guardar los datos de hombres y mujeres en diferentes hojas del mismo archivo Excel
with pd.ExcelWriter('data/datos_hombres_mujeres_5_a_9.xlsx') as writer:
    datos_hombres.to_excel(writer, sheet_name='Hombres')
    datos_mujeres.to_excel(writer, sheet_name='Mujeres')

print("Datos guardados exitosamente en 'data/datos_hombres_mujeres_5_a_9.xlsx'")

# Mostrar los resultados
print(f"Media de hombres (De 5 a 9 años): {media_hombres_porBarrio}")
print(f"Media de mujeres (De 5 a 9 años): {media_mujeres_porBarrio}")

print(f"Varianza de hombres (De 5 a 9 años): {varianza_hombres_porBarrio}")
print(f"Varianza de mujeres (De 5 a 9 años): {varianza_mujeres_porBarrio}")

print(f"Moda de hombres (De 5 a 9 años): {moda_hombres_porBarrio}")
print(f"Moda de mujeres (De 5 a 9 años): {moda_mujeres_porBarrio}")

# Guardar los datos concatenados en un archivo de texto
guardar_datos_concatenados(barrios, datos_hombres, datos_mujeres, 'data/lista.txt')

# prueba de la clase PoblacionBarrio

# crear cinco objetos de la clase PoblacionBarrio para cinco barrios
objetos_barrio = []
for i, barrio in enumerate(barrios[:5]):
    obj = PoblacionBarrio(barrio, datos_hombres[i], datos_mujeres[i])
    objetos_barrio.append(obj)

# Imprimir los objetos
print("\n=== Imprimiendo objetos de la clase PoblacionBarrio ===")
for obj in objetos_barrio:
    print(obj)

# Modifica un valor de prueba (núm de hombres en el primer barrio)
objetos_barrio[0].set_modificar_barrio("pacifico")
print(f"\nModificado: {objetos_barrio[0]}")

# Compara dos objetos
print(f"\nComparación de {objetos_barrio[0].nombre_barrio} y {objetos_barrio[1].nombre_barrio}: {objetos_barrio[0] < objetos_barrio[1]}")

# Suma y resta dos objetos
suma = objetos_barrio[0] + objetos_barrio[1]
resta = objetos_barrio[0] - objetos_barrio[1]

print(f"\nSuma de {objetos_barrio[0].nombre_barrio} y {objetos_barrio[1].nombre_barrio}: {suma}")
print(f"\nResta de {objetos_barrio[0].nombre_barrio} y {objetos_barrio[1].nombre_barrio}: {resta}")


