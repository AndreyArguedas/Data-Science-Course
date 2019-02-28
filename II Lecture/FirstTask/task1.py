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

import math

def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    acum = 0
    med = media(lista)
    for i in lista:
        acum += (i - med) ** 2 
    return acum / len(lista)

def desviacion(lista):
    return math.sqrt(varianza(lista))

print(media(y))
print(varianza(y))
print(desviacion(y))


# Calcule la media, la varianza y la desviacio´n est´andar de x.

print(media(x))
print(varianza(x))
print(desviacion(x))

# Calcule la correlaci´on entre x y y.   //Volver a checkear este ejercicio
import numpy as np
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

print(datos_est.iloc[:,:2])

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
"""
import numpy as np
dictionary = {}
cuants = datos_est.select_dtypes(include=['float64', 'int64'])
for i in range(0, cuants.shape[1]):
    minimo = np.min(cuants.iloc[:,i])
    maximo = np.max(cuants.iloc[:,i])
    media = np.mean(cuants.iloc[:,i])
    mediana = np.median(cuants.iloc[:,i])
    dictionary[cuants.columns.values[i]] = { 'Minimo' : minimo, 'Maximo' : maximo, 'Media' : media, 'Mediana' : mediana}

chd = datos_est.loc[:,'chd']
print(chd)

yesAnswer = 0
noAnswer = 0
for i in range(0, chd.shape[0]):
    if chd.loc[i, 1] == "Si":
        yesAnswer += 1
    else:
        noAnswer += 1
dictionary['chd'] = {'Si' : yesAnswer, 'No' : noAnswer}
print(dictionary)
"""

"""
10. Suponga que tenemos en una lista las notas de un estudiante en 3 ex´amenes, por ejemplo notas
= (90,45,89), luego escriba instrucciones en Python para calcular el promedio y se despliegue
“Gan´o el curso” si la nota es mayor o igual a 67.5, “Extraordinario” si la nota es mayor o igual
a 47.5 y menor a 67.5, “Perdi´o el curso” si la nota es menor a 47.5.
"""

notas = (90,45,89)
promedio = np.average(notas)
if promedio < 47.5:
    print("Perdió el curso")
elif promedio >= 47.5 and promedio < 67.5:
    print("Extraordinario")
elif promedio >= 67.5:
    print("Ganó el curso")

"""
11. Escriba instrucciones en Python tal que dada la lista lista = (-9,-45,0,7,45,-100,89),
calcule la suma de los n´umeros positivos, la suma de los n´umeros negativos en valor absoluto
y al final despliegue la suma m´as grande.
"""

lista = (-9,-45,0,7,45,-100,89)
positivos = list(filter(lambda e: e >= 0, lista))
negativos = list(filter(lambda e: e < 0, lista))
negativos = list(map(lambda e: abs(e), negativos))
sumaPos = sum(positivos)
sumaNeg = sum(negativos)
if sumaPos > sumaNeg:
    print("Suma Positivos es mayor :", sumaPos)
elif sumaPos == sumaNeg:
    print("Sumas son iguales :", sumaPos)
else:
    print("Sumas Negativos es mayor :", sumaNeg)

"""
12. Programe en Python una funci´on que recibe dos valores, determinar cu´al de los dos valores es
el menor y luego lo retorna (no puede usar la funci´on min de Python).
"""

def menor(v1, v2):
    return v1 if v1 <= v2 else v2

print("El menor de 34 y 87 es: ", menor(34, 87))
print("El menor de 541 y 5 es: ", menor(541, 5))


"""
13 Programe en Python una función que recibe tres valores A, B, y C y 
retorna el menor (no puede usar la función min de Python)
"""

def menorDe3(a, b, c):
    minimum = menor(a, b)
    return c if c <= minimum else minimum

print("El menor de 34, 56 y 87 es: ", menorDe3(34, 56, 87))

"""
14. Programe en Python una funci´on que recibe cuatro n´umeros y retorna el mayor (no puede usar
la funci´on max de Python).
"""

def mayor(v1, v2, v3, v4):
    argsExcFirst = (v2, v3, v4)
    maximum = v1
    for i in argsExcFirst:
        maximum = i if i >= maximum else maximum
    return maximum

mayor(58, 63, 1, 987)
    

"""
15. Programe en Python una función que recibe un n´umero n y retorna la sumatoria de los n´umeros
enteros comprendidos entre el 1 y el n.
"""
def sumatoria(num):
    accum = 0
    for i in range(1, num + 1):
        accum += i
    return accum

sumatoria(6)


"""
6. Desarrolle una funci´on que realice la sumatoria de los n´umeros enteros pares comprendidos
entre el 1 y el n.
"""

def sumaPares(num):
    accum = 0
    for i in filter(lambda e: e %2 == 0, range(1, num + 1)):
        accum += i
    return accum

sumaPares(6)

"""
17. Desarrolle una funci´on que realice la sumatoria de los n´umeros enteros m´ultiplos de 5, 
    comprendidos entre el 1 y el n.
"""

def sumaMultiplos(num):
    accum = 0
    for i in filter(lambda e: e % 5 == 0, range(1, num + 1)):
        accum += i
    return accum

sumaMultiplos(10)

"""
18. Programe en Python una funci´on que genera 200 n´umeros al azar entre 1 y 500 y luego calcula
cu´antos est´an entre el 50 y 450, ambos inclusive.
"""

def genRandNums():
    from random import randint
    nums = [randint(1, 500) for p in range(0, 200)]
    return len(list(filter(lambda e: e in range(50, 450), nums)))

genRandNums()

"""
19. Desarrolle una funci´on que calcula el costo de una llamada telef´onica que ha durado t minutos
sabiendo que si t < 1 el costo es de 0,4 d´olares, mientras que para duraciones superiores el
costo es de 0,4 + (t − 1)/4 d´olares, la funci´on debe recibir el valor de t.
"""

def calculaCosto(t):
    return 0.4 if t < 1 else 0.4 + (t - 1) / 4

print("El costo de una llamada de 0.9 minutos es: ", calculaCosto(0.9))
print("El costo de una llamada de 5 minutos es: ", calculaCosto(5))


"""
20. Desarrolle una funci´on que reciba un vector de n´umeros reales y un n´umero real x, tal que
indique el porcentaje de elementos menores o iguales a un valor x.
"""

def porcentajeMenores(vec, x):
    menores = list(filter(lambda e: e <= x, vec))
    return (len(menores) / len(vec)) * 100

vecPrueba = [ 4, 50, 147, 2, 35, 70, 94]
print("El porcentaje de #'s menores o iguales a 50 es :", porcentajeMenores(vecPrueba, 50))
      
"""
21. Desarrolle una funci´on que reciba un n´umero natural n (suponiendo que n > 1) y que construya
y retorne un vector v de tama˜no n tal que vk =
vk−1
3 +0,5 para k = 2, . . . , n y siendo que v1 = 1.
"""

def construyeVec(n, vec = []):
    if n <= 1:
        vec.append(1)
        return vec
    else:
        result =  construyeVec(n - 1, vec)[-1] / 3 + 0.5
        vec.append(result)
        return vec

print("El resultado para k=4 es: ", construyeVec(4))

"""
22. Desarrolle una función que recibe una matriz cuadrada A de tamaño n × n y calcula su traza,
es decir, la suma de los elementos de la diagonal. Por ejemplo, la traza de la siguiente matriz:
9 3 4
1 3 −1
4 12 −2

es 10.
"""

def traza(matriz):
    traza = 0
    for i in range(len(matriz)):
        traza += matriz[i][i]
    return traza
            
m1 = [[9, 3, 4], [1, 3, -1], [4, 12, -2]]
print("La traza es de: ", traza(m1))


"""
23. Desarrolle una función en Python que recibe un DataFrame que retorna la cantidad 
de entradas de este DataFrame que son divisibles entre 3 (Pruebe esta funci´on leyendo un archivo
de datos, esto en el Script de pruebas).
"""


import os
import pandas as pd
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")
pd.set_option('display.max_columns', 6)
pd.set_option('display.width', 1000)
data = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
print(data)

def divisibles(datos):
    acum = 0
    for i in range(datos.shape[0]):
        for j in range(datos.shape[1]):
            if datos.iloc[i, j] % 3 == 0:
                acum += 1
    return acum;

print("El numero de divisibles entre 3 es: ", divisibles(data))


"""
24. Desarrolle una funci´on en Python que recibe un DataFrame y dos n´umeros de columna y
que retorna en una lista con el nombre de las variables correspondientes a las columnas, la
covarianza y la correlaci´on entre esas dos variables (Pruebe esta funci´on leyendo un archivo de
datos, esto en el Script de pruebas).
"""

import os
import pandas as pd
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")
pd.set_option('display.max_columns', 6)
pd.set_option('display.width', 1000)
data = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)

def covarianza(data, c1, c2):
    covar = data.iloc[:, c1].cov(data.iloc[:, c2])
    corre = data.iloc[:, c1].corr(data.iloc[:, c2])
    return {"Covarianza" : covar, "Correlacion" : corre }
    
covarianza(data, 0, 1)