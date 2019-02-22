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
