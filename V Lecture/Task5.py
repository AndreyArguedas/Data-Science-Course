# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:30:06 2019

@author: Andrey
"""

# Ejercicio 1

#1.a

import os
import pandas as pd
import numpy as np

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/V Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('Titanic.csv',delimiter=',',decimal=",",index_col=0)
print(datos)


#1.b

def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod

datos["Survived"] = recodificar(datos["Survived"], {0:'No',1:'Yes'})
datos["Pclass"] = recodificar(datos["Pclass"], {1:'First',2:'Second',3:'Third'})
datos["Embarked"] = recodificar(datos["Embarked"], {'C':'Cherbourg', 'Q':'Queenstown','S':'Southampton'})

print(datos.head())

print("******************************\n")

print(datos['Survived'].value_counts())

print("******************************\n")

print(datos['Pclass'].value_counts())

print("******************************\n")

print(datos['Embarked'].value_counts())


#1.c

print("******************************\n")

print("Describe")

print(datos.dropna().describe())

print("******************************\n")

print("Means")

print(datos.mean(numeric_only=True))

print("******************************\n")

print("STDs")

print(datos.median(numeric_only=True))

print("******************************\n")

print("Maximo")

print(datos.max(numeric_only=True))

print("******************************\n")

print("Percentiles")

print(datos.quantile(np.array([0,.25,.50,.75,1])))

print("******************************\n")

print("Datos en variables categóricas\n")

print("Sobrevivientes:")

print(datos['Survived'].value_counts())

print("******************************\n")

print("Clase:")

print(datos['Pclass'].value_counts())

print("******************************\n")

print("Puerto en el que embarcó:")

print(datos['Embarked'].value_counts())

print("******************************\n")

print("TABLA CRUZADA - Supervivencia por clase:")

survived_pclass = pd.crosstab(index=datos["Survived"], columns=datos["Pclass"])
print(survived_pclass)

print("******************************\n")

print("TABLA CRUZADA - Supervivencia por puerto de embarco:")

survived_pclass = pd.crosstab(index=datos["Survived"], columns=datos["Embarked"])
print(survived_pclass)

print("TABLA CRUZADA - Supervivencia por genero:")

survived_pclass = pd.crosstab(index=datos["Survived"], columns=datos["Sex"])
print(survived_pclass)