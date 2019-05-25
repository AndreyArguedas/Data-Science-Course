# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:14:22 2019

@author: Andrey
"""

# Ejercico 2

import os
import pandas as pd
import numpy as np
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import math

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VII Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('Titanic.csv',delimiter=',',decimal=".",index_col=0)

def recodificar(col, nuevo_codigo):
  col_cod = pd.Series(col, copy=True)
  for llave, valor in nuevo_codigo.items():
    col_cod.replace(llave, valor, inplace=True)
  return col_cod

datos["Sex"] = recodificar(datos["Sex"], {'male':0, 'female':1})
datos["Embarked"] = recodificar(datos["Embarked"], {'C':1, 'Q':2,'S':3})

del[datos["Name"]]
del[datos["Ticket"]]
del[datos["Fare"]]
del[datos["Cabin"]]
del[datos["Age"]]

print(datos.head())

#2.2

# Se dejan las variables predictorias en una tabla

X = datos.iloc[:,1:] 
print(X.head())

# Se separa las variablea a predecir

y = datos.iloc[:,0:1] 
print(y.head())


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)

print("========Tabla de entrenamiento========")

print(X_train.head())

print("========Tabla de test========")

print(X_test.head())

print("========Tabla de entrenamiento a predecir========")

print(y_train.head())


print("========Tabla de test a predecir========")

print(y_test.head())



#3 Aplicando KNN

# Primero sacar k

cantidad = X_train.shape[0]

k = math.sqrt(cantidad)

k = math.trunc(k)

instancia_knn = KNeighborsClassifier(n_neighbors=k)

instancia_knn.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn.score(X_test, y_test)))


#4

prediccion = instancia_knn.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

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

indices = indices_general(MC,list(np.unique(y)))
    
for k in indices:
    print("\n%s:\n%s"%(k,str(indices[k])))
    
#Extrayendo precisiones

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
p = precisiones(MC)

for k in p:
    print("\n%s:\n%s"%(k,str(p[k])))
    