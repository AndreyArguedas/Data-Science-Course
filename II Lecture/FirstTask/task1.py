# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:01:51 2019

@author: Andrey
"""

print("Hello Anaconda")

""" 
1. Dado x = (3,−5,31,−1,−9,10,0,18) y 
   dado y = (1,1,−3,1,−99,−10,10,−7) 
   realice lo siguiente
"""

# Introduzca x y y como listas en Python.

x = [3,-5,31,-1,-9,10,0,18]
y = [1,1,-3,1,-99,-10,10,-7]

print(x)
print(y)

# Calcule la media, la varianza y la desviacio´n est´andar de y.

import numpy as np

media = np.mean(y)
deviacion = np.std(y)
varianza = np.var(y)

print(media)
print(deviacion)
print(varianza)

# Calcule la media, la varianza y la desviacio´n est´andar de x.

media = np.mean(x)
deviacion = np.std(x)
varianza = np.var(x)

print(media)
print(deviacion)
print(varianza)

# Calcule la correlaci´on entre x y y.   //Volver a checkear este ejercicio

np.corrcoef(x, y)

# Escriba comandos en Python para extraer las entradas 2 a la 7 de x.

x[2:8]

# Escriba comandos en Python para extraer las entradas de y excepto la 2 y la 7.

list(filter(lambda e : y.index(e) not in (2, 7), y))

# Escriba comandos en Python para extraer las entradas de y menores a -3 o mayores a 10.

list(filter(lambda e: e < -3 or e > 10, y))

# Escriba comandos en Python para extraer las entradas de x mayores a 0 y que sean n´umeros pares.

list(filter(lambda e: e > 0 and e % 2 == 0, x))

""" 
2. Usando c´odigo Python (no archivos) en un DataFrame la siguiente tabla de datos:
"""

"""
Peso Edad Nivel Educativo
76 25 Lic
67 23 Bach
55 19 Bach
57 18 Bach
87 57 Dr
48 13 MSc
"""

import pandas as pd

datos = {'Peso': [76, 67, 55, 57, 87, 48],
         'Edad': [25, 23, 19, 18, 57, 13],
         'Nivel Educativo': ["Lic", "Bach", "Bach", "Bach", "Dr", "MSc"]
         }
datos_pandas = pd.DataFrame(datos)
print(datos_pandas)

"""
3. Genere una hoja de datos (“data frame”) a partir de la siguiente tabla de datos y verifique que
las variables tengan el tipo de dato adecuado

id: Identificador ´unico del estudiante.
calificacion: Nota o calificaci´on obtenida en una escala descendente de la A a la D.
duracion: Cantidad de minutos requeridos para realizar la prueba.

id calificacion duracion
1 B 64
2 C 85
3 B 76
4 A 83
5 A 80
6 A 78
7 C 68
8 B 82
9 A 89
10 B 61

"""

datos = {'calificacion': ["B", "C", "B", "A", "A", "A", "C", "B", "A", "B"],
         'duracion': [64, 85, 76, 83, 80, 78, 68, 82, 89, 61]
         }
datos_pandas = pd.DataFrame(datos)
datos_pandas.index = np.arange(1,len(datos_pandas)+1)
datos_pandas.index.name = "id"
print(datos_pandas)

"""
4. Dado x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40) realice las siguiente operaciones:
"""

#Indique los ´ındices de los valores o entradas del vector cuya divisi´on entre 2 tiene como resultado 45.









