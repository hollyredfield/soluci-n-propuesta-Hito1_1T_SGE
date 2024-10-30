# Archivo de documentación sobre el proyecto
Proyecto: Análisis de la Población por Edad y Sexo en los Barrios del Distrito de Retiro en la ciudad de Madrid

Descripción del Proyecto
Este proyecto tiene como objetivo realizar un análisis de la población por edad y sexo en los barrios del distrito de Retiro en Madrid y se focaliza en un barrio y un rango de edad concretos.


El análisis incluye:

Descarga de un archivo Excel con datos estadísticos.
Limpieza de los datos y transformación de filas por columnas.
Cálculo de estadísticas básicas (media, varianza, moda) sobre los datos.
Uso de Programación Orientada a Objetos (POO) para modelar y manipular los datos de los barrios.
Almacenamiento de los resultados en archivos Excel y texto.

Estructura del Proyecto
El proyecto está organizado en los siguientes directorios y archivos:

Directorios:
data/: Contiene los archivos Excel descargados y generados, así como el archivo de texto con los datos concatenados.
scripts/: Contiene los archivos Python con las funciones y clases del proyecto.

Archivos:
main.py: Script principal que coordina todo el flujo del programa, desde la descarga de datos hasta la impresión de los resultados.

data/
data/Retiro_Poblacion por Edad y Sexo.xlsx: Archivo Excel descargado de la página web con los datos iniciales.
data/df_transformado.xlsx: Archivo Excel generado con los datos transformados.
data/datos_hombres_mujeres_5_a_9.xlsx: Archivo Excel con los datos de hombres y mujeres de la categoría "De 5 a 9 años".
data/lista.txt: Archivo de texto con los datos concatenados de los barrios.

scripts/
scripts/descarga_datos.py: Script para descargar el archivo Excel de la web.
scripts/limpieza_datos.py: Script para limpiar los datos (eliminar filas irrelevantes, manejar valores NaN, etc.).
scripts/transformacion_datos.py: Script para transformar los datos (cambiar filas por columnas).
scripts/estadisticas_poblacion.py: Script que contiene la clase EstadisticasPoblacion para calcular media, varianza y moda.
scripts/poblacion_barrio.py: Script que contiene la clase PoblacionBarrio para modelar los datos de los barrios.
scripts/guardar_datos.py: Script para guardar los datos concatenados en un archivo de texto.

Requisitos
Para ejecutar el proyecto es necesario tener instalados los siguientes paquetes de Python:

pandas: Para el manejo y manipulación de datos en formato Excel.
requests: Para la descarga del archivo Excel desde la web.
Puedes instalar estos paquetes utilizando 'pip install pandas requests'

Ejecución del Proyecto
Sigue los siguientes pasos para ejecutar el proyecto:

Descargar el archivo Excel: El script main.py descargará automáticamente el archivo Excel desde la web del Ayuntamiento de Madrid con los datos de población por edad y sexo en el distrito de Retiro.

Limpieza y transformación de los datos: Los datos son limpiados y transformados utilizando las funciones en los scripts del directorio scripts/, y verifica la integridad y adecuación de la información.

Cálculo de estadísticas: El programa calcula la media, varianza y moda de los datos seleccionados (de hombres y mujeres, por barrio).

Programación Orientada a Objetos (POO): Se crea la clase PoblacionBarrio para modelar y manipular los datos de cada barrio.

Guardado de los resultados: Los resultados del análisis son guardados en archivos Excel y en un archivo de texto (lista.txt).

Para ejecutar el proyecto, simplemente corre el archivo main.py

Resultados Esperados
Al ejecutar el programa, se generarán los siguientes archivos en el directorio data/:

df_transformado.xlsx: Datos transformados del archivo original.
datos_hombres_mujeres_5_a_9.xlsx: Datos de hombres y mujeres de la categoría "De 5 a 9 años" por barrio.
lista.txt: Archivo de texto con los datos concatenados de los barrios.

El programa también imprimirá por consola:

Los resultados de la transformación y limpieza de datos.
Las estadísticas calculadas (media, varianza, moda).
La prueba de la clase PoblacionBarrio (impresión de objetos, modificación de atributos, comparación, suma y resta de objetos).

Ilustraciones
=== Imprimiendo objetos de la clase PoblacionBarrio ===
Barrio: Pacífico
Hombres: 547
Mujeres: 535
Barrio: Adelfas
Hombres: 364
Mujeres: 409
Barrio: Estrella
Hombres: 495
Mujeres: 457
Barrio: Ibiza
Hombres: 387
Mujeres: 425
Barrio: Los Jerónimos
Hombres: 155
Mujeres: 124

Modificado: Barrio: pacifico
Hombres: 547
Mujeres: 535

Comparación de pacifico y Adelfas: False

Suma de pacifico y Adelfas: Barrio: pacifico
Hombres: 911
Mujeres: 944

Resta de pacifico y Adelfas: Barrio: pacifico
Hombres: 183
Mujeres: 126

Contribuciones
Este proyecto ha sido desarrollado con fines educativos y es un ejercicio para repasar conceptos de programación en Python, manejo de datos, y Programación Orientada a Objetos, sobre la base del Hito 1_1T_2DAM para la asignatura de Sistemas de Gestión Empresarial.

Se anima a los estudiantes a mejorar y expandir el proyecto con nuevas funcionalidades, excediendo los requerimientos planteados por el Hito.

El ejercicio se ha realizado en VSCode y el fichero descargado ha sido seleccionado con fines didácticos, todo lo cual no tiene porqué corresponder con las instrucciones del ejercicio oficial aquí mencionado.
