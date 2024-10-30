# Punto Introducción a la POO
# Crea una clase que tenga como atributos las columnas del dataset

class PoblacionBarrio:
    def __init__(self, nombre_barrio, hombres, mujeres):
        self.nombre_barrio = nombre_barrio
        self.hombres = hombres
        self.mujeres = mujeres

    # Define una forma de imprimir los objetos de la clase, mostrando todos los datos de los atributos de forma clara
    def __str__(self):
        return f"Barrio: {self.nombre_barrio}\nHombres: {self.hombres}\nMujeres: {self.mujeres}"
    
    # Crea métodos para modificar el valor de cada atributo de la clase
    def set_modificar_barrio(self, nuevo_barrio):
        self.nombre_barrio = nuevo_barrio

    def set_modificar_hombres(self, nuevo_valor):
        self.hombres = nuevo_valor

    def set_modificar_mujeres(self, nuevo_valor):
        self.mujeres = nuevo_valor

    # Redefine los métodos especiales de comparación para poder comparar los objetos de la clase por el valor de la segunda columna (población de hombres)
    def __lt__(self, otro):
        return self.hombres < otro.hombres
    
    def __eq__(self, otro):
        return self.hombres == otro.hombres
    
    # Redefine los métodos de suma y resta para que devuelvan el valor de la suma o resta de cada atributo
    def __add__(self, otro):
        suma_hombres = self.hombres + otro.hombres
        suma_mujeres = self.mujeres + otro.mujeres
        return PoblacionBarrio(self.nombre_barrio, suma_hombres, suma_mujeres)
    
    def __sub__(self, otro):
        resta_hombres = self.hombres - otro.hombres
        resta_mujeres = self.mujeres - otro.mujeres
        return PoblacionBarrio(self.nombre_barrio, resta_hombres, resta_mujeres)
    
    # Crea un objeto de la clase para al menos cinco filas y prueba todos tus métodos --> main.py



