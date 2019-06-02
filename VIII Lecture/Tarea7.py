# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:14:07 2019

@author: Andrey
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from   sklearn.model_selection import train_test_split
from   sklearn.neural_network import MLPClassifier
from   sklearn.metrics import confusion_matrix
import math

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VIII Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('titanic.csv',delimiter=',',decimal=".",index_col=0)

def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod

datos["Survived"] = recodificar(datos["Survived"], {0 : 'No', 1: 'Yes'})

datos['Pclass'] = datos['Pclass'].astype('category')
datos['Sex'] = datos['Sex'].astype('category')
datos['Embarked'] = datos['Embarked'].astype('category')

datos["Sex"] = datos["Sex"].cat.codes
datos["Embarked"] = datos["Embarked"].cat.codes
datos["Pclass"] = datos["Pclass"].cat.codes

datos['Sex'] = datos['Sex'].astype('category')
datos['Embarked'] = datos['Embarked'].astype('category')
datos['Pclass'] = datos['Pclass'].astype('category')

del[datos["Name"]]
del[datos["Ticket"]]
del[datos["Cabin"]]

#Imputando la edad con la moda
datos = datos.fillna(np.mean(datos))

print(datos.head())

print(datos.info())


#1.b

# Se dejan las variables predictorias en una tabla

X = datos.iloc[:,1:] 
print(X.head())

# Se separa las variablea a predecir

y = datos.iloc[:,0:1] 
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)

print(X_train.head())

print(X_test.head())

print(y_train.head())

print(y_test.head())

#1.c

#100 nodos
instancia_red = MLPClassifier(solver='lbfgs', random_state=0)
print(instancia_red)

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))

# 50 capas, 50 nodos
instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[50, 50])

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))


# 500 capas, 500 nodos
instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[500, 500])

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))


#1000 capas, 1000 nodos

instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[1000, 1000])

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))

#Mejor resultado

instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[20, 20])

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))