# Operaciones y estadísticas

import pandas as pd

class EstadisticasPoblacion:
    def __init__(self, datos_hombres, datos_mujeres, barrios):
        self.datos_hombres = datos_hombres
        self.datos_mujeres = datos_mujeres
        self.barrios = barrios

    def calcular_media(self):
        # Es el promedio aritmético: suma de todos los valores, dividida por la cantidad de valores
        media_hombres_porBarrio = round(self.datos_hombres.mean())
        media_mujeres_porBarrio = round(self.datos_mujeres.mean())
        return media_hombres_porBarrio, media_mujeres_porBarrio
    
    def calcular_varianza(self):
        # dispersión de los datos (cuánto se alejan de la media); si es alta, > dispersión
        varianza_hombres_porBarrio = round(self.datos_hombres.var())
        varianza_mujeres_porBarrio = round(self.datos_mujeres.var())
        return varianza_hombres_porBarrio, varianza_mujeres_porBarrio
    
    def calcular_moda(self):
        # valor que aparece más veces en la lista de datos; si no hay repeticiones, pandas nos muestra el menor
        moda_hombres_porBarrio = self.datos_hombres.mode()[0]
        moda_mujeres_porBarrio = self.datos_mujeres.mode()[0]
        return moda_hombres_porBarrio, moda_mujeres_porBarrio