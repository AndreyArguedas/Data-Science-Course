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

x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40)
indices = []
for element in x:
    if element / 2 == 45:
        indices.append(x.index(element))

print(indices)

# Indique el ´ındice del valor m´as alto del vector.

x.index(max(x))

# Indique el resultado de la suma de los valores (entradas del vector) menores a la media del vector.

"""
    Version utilizando reduce
"""
from functools import reduce

media = np.mean(x)

reduce((lambda x, y: x + y), list(filter(lambda e: e < media, x)))

# Utilizando el operador l´ogico and (“y”l´ogico) indique cu´ales los valores del vector que son mayores a la media del vector y que sean divisibles entre 2.

media = np.mean(x)

list(filter(lambda e: e > media and e % 2 == 0, x))


"""
5. Para las variables almacenadas de la siguiente forma v1 = (2,7,6,4,52), v2 = (7,5,7,0,1))
y v3 = (2,4,3,5,6) usando el comando sum calcule la sumatoria de cada una de esas variables.
Repita lo anterior usando un for(...).
"""

v1 = (2,7,6,4,52)
v2 = (7,5,7,0,1)
v3 = (2,4,3,5,6)

print("Sum v1", sum(v1))

print("Sum v2", sum(v2))

print("Sum v3", sum(v3))

def suma(v):
    acum = 0
    for i in v:
        acum += i
    return acum

print("--------------------")

print("Suma v1", suma(v1))

print("Suma v2", suma(v2))

print("Suma v3", suma(v3))

"""
6. Dado x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40) construya una lista llamada lista1 que
tenga 3 campos Media, M´aximo y M´ınimo que tienen la media, el m´aximo y el m´ınimo respectivamente del vector x.
"""

x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40)
lista1 = [np.mean(x), max(x), min(x)]
print(lista1)

"""
Escriba el c´odigo Python necesario para efectuar la siguiente operaci´on entre matrices:

"""

import numpy as np

M1 = np.matrix([[9, 3, 4], [1, 3, -1]])
M2 = np.matrix([[91, -3], [1, 8], [-4, 5]])
A = M1 + 2 * np.transpose(M2)
print(A)

"""
8. Cargue en un DataFrame el archivo EjemploAlgoritmosRecomendacion.csv y haga lo siguiente:
"""

import os
import pandas as pd
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
datos_est = pd.read_csv('EjemploAlgoritmosRecomendacion.csv',delimiter=';',decimal=",",index_col=0)
print(datos_est)

# Calcule la dimensi´on de la Tabla de Datos.
dimension = datos_est.shape
print("Dimension: " + str(dimension[0]) + " x " + str(dimension[1]))

# Despliegue las primeras 2 columnas de la tabla de datos.

print(datos_est.iloc[:,:1])

# Ejecute un info() de los datos.

datos_est.info()

# Calcule la Media para todas las variables cualesquiera.
import numpy as np
dictionary = {}
columns = datos_est.shape[1]
for i in range(0,columns):
    media = np.mean(datos_est.iloc[:,i])
    dictionary[datos_est.columns.values[i]] = media
print(dictionary)

"""
9. Cargue la tabla de datos que est´a en el archivo SAheartv.csv haga lo siguiente:
"""    

import os
import pandas as pd
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
datos_est = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos_est)

# Calcule la dimensión de la Tabla de Datos.
dimension = datos_est.shape
print("Dimension: " + str(dimension[0]) + " x " + str(dimension[1]))

# Despliegue las primeras 3 columnas de la tabla de datos

print(datos_est.iloc[:,:2]) 

#Ejecute un info de los datos

datos_est.info()

# Calcule la suma de las columnas con variables cuantitativas (num´ericas).

import numpy as np
cuants = datos_est.select_dtypes(include=['float64', 'int64'])
dictionary = {}
for i in range(0, cuants.shape[1]):
    suma = np.sum(cuants.iloc[:,i])
    dictionary[cuants.columns.values[i]] = suma
print(dictionary)

# Calcule para todas las variables cuantitativas presentes en el archivo SAheart.csv: 
#El m´ınimo, el m´aximo, la media, la mediana y para la variables chd determine 
#la cantidadde Si y de No.

import numpy as np
dictionary = {}
for i in range(0, datos_est.shape[1]):
    minimo = np.min(datos_est.iloc[:,i])
    maximo = np.max(datos_est.iloc[:,i])
    media = np.mean(datos_est.iloc[:,i])
    mediana = np.median(datos_est.iloc[:,i])
    dictionary[datos_est.columns.values[i]] = { 'Minimo' : minimo, 'Maximo' : maximo, 'Media' : media, 'Mediana' : mediana}
    
print(dictionary)