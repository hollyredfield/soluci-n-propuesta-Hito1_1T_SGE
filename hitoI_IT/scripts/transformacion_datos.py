# Script para transformar los datos

import pandas as pd

class TransformarDatos:
    def __init__(self, df):
        self.df = df

    def cambiar_filas_por_columnas(self):
        # Cambiar las filas por columnas (trasponer)
        self.df = self.df.transpose()

        return self.df
    
    def ajustar_indice(self):
        """
        Ignoramos la primera columna 'Unnamed' y ajustamos el índice con los nombres de los barrios.
        """
        # Establecer la segunda columna (barrios) como índice, ignorando la primera columna Unnamed
        self.df = self.df.set_index(self.df.columns[0])
        return self.df
    
    def extraer_datos_por_rango_edad(self, columna_hombres, columna_mujeres, index_inicio, index_fin):
        """
        Extrae los datos de una categoría de edad específica tanto para hombres como para mujeres, 
        excluyendo la fila del distrito completo (índice 2) y sumando solo las filas de los barrios (índices 3-8).
        """
        # Extraer los datos de hombres (columna E) y mujeres (columna AB) en los barrios (índices 3-8)
        datos_hombres = self.df.iloc[index_inicio:index_fin + 1, columna_hombres]
        datos_mujeres = self.df.iloc[index_inicio:index_fin + 1, columna_mujeres]

        return datos_hombres, datos_mujeres


 
