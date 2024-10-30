# Script para limpiar los datos

import pandas as pd

# Función para cargar el archivo Excel (dataset)
def cargar_dataset(ruta_archivo):
    return pd.read_excel(ruta_archivo, engine='openpyxl')

# Función para eliminar filar irrelevantes
def eliminar_filas(df, filas_a_eliminar):
    return df.drop(df.index[filas_a_eliminar])

# Eliminar las primeras 5 filas que no contienen datos relevantes
# df_clean = df.drop(index=[0, 1, 2, 3, 6, 8, 31, 33, 56, 58, 81])

# Función para eliminar la primera columna, vacía
def eliminar_primera_columna(df):
    return df.drop(df.columns[0], axis = 1)


# Función para reemplazar valores NaN por 0 y verificar que no queden valores NaN
def reemplazar_nan(df):
    df = df.fillna(0)
    return df

# Función para verificar valores inconsistentes (< 0, texto en campos numéricos)
def verificar_datos_inconsistentes(df):

    # Seleccionamos columnas numéricas (de acuerdo con el dataset)
    columnas_numericas = df.select_dtypes(include=['number']).columns

    # Verificar si hay valores menores a 0 en columnas numéricas y convertir a 0
    valores_negativos = df[columnas_numericas] < 0
    if valores_negativos.any().any():
        print("Atención: hay valores negativos en las columnas numéricas")
        print(df[valores_negativos])
        df[columnas_numericas] = df[columnas_numericas].applymap(lambda x: 0 if x < 0 else x)

    # Verificar si hay texto en columnas numéricas

    for col in columnas_numericas:

        # detectar valores no numércios en columna numérica
        no_numerico = pd.to_numeric(df[col], errors='coerce').isna() & df[col].notna()
        if no_numerico.any():
            print(f"Atención: hay texto en la columna numérica '{col}'")
            print(df[no_numerico])

        # convertir todo valor no numérico detectado en 0
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)


    return df



    
