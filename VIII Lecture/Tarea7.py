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

#1.d

def indices_general(MC, nombres = None):
    precision_global = np.sum(MC.diagonal()) / np.sum(MC)
    error_global = 1 - precision_global
    precision_categoria  = pd.DataFrame(MC.diagonal()/np.sum(MC,axis = 1)).T
    if nombres!=None:
        precision_categoria.columns = nombres
    return {"Matriz de Confusión":MC, 
            "Precisión Global":precision_global, 
            "Error Global":error_global, 
            "Precisión por Categoría":precision_categoria}
    
def precisiones(MC):
    VN = MC[0][0]
    FP = MC[0][1]
    FN = MC[1][0]
    VP = MC[1][1]
    
    return {"Precision Global": (VN + VP) / (VN + FP + FN + VP), 
            "Precisión Positiva": VP / (FN + VP), 
            "Precisión Negativa": VN / (VN + FP), 
            "Precisión Falsos Positivos": FP / (VN + FP),
            "Precisión Falsos Negativos": FN / (VP + FN),
            "Asertividad Positiva": VP / (FP + VP),
            "Asertividad Negativa": VN / (FN + VN)}

def resumenMatrizPrecisiones(instancia, X_testP, y_testP, yP):
    prediccion = instancia.predict(X_testP)
    MC = confusion_matrix(y_testP, prediccion)
    indices = indices_general(MC,list(np.unique(yP)))
    
    for k in indices:
        print("\n%s:\n%s"%(k,str(indices[k])))
    
    #Extrayendo precisiones

    p = precisiones(MC)

    for k in p:
        print("\n%s:\n%s"%(k,str(p[k])))
        
print("Matriz de confusion y precisiones")

resumenMatrizPrecisiones(instancia_red, X_test, y_test, y)