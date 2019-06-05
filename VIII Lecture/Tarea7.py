# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:14:07 2019

@author: Andrey
"""

import os
import pandas as pd
import numpy as np
import mglearn
from sklearn.model_selection import train_test_split
from   sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential      
from keras.layers import Dense
from keras.layers import Reshape
from   sklearn.metrics import confusion_matrix

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




#100 nodos
instancia_red = MLPClassifier(solver='lbfgs', random_state=0)

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

print("Matriz de confusion y precisiones")

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

resumenMatrizPrecisiones(instancia_red, X_test, y_test, y)


#Version de KERAS

dummy_y = pd.get_dummies(y)
dummy_X = pd.get_dummies(X)

print(dummy_X.head())
print(dummy_y.head())

scaler = MinMaxScaler(feature_range = (0, 1))
scaled_dummy_X  = pd.DataFrame(scaler.fit_transform(dummy_X), columns = list(dummy_X))

X_train, X_test, y_train, y_test = train_test_split(scaled_dummy_X, dummy_y, train_size=0.75, random_state = 0)

print(X_train.head())
print(X_test.head())

print(y_train.head())
print(y_test.head())

model = Sequential()
model.add(Dense(26, input_dim = 13, activation = 'relu'))  # Agregamos primera capa oculta
model.add(Dense(11, activation = 'relu'))  # Agregamos primera capa oculta
model.add(Dense(6, activation = 'relu'))  # Agregamos tercera capa oculta
model.add(Dense(2, activation = 'sigmoid')) # Agregamos capa output

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

print(model.summary())

model.fit(X_train, y_train, epochs = 78, batch_size = 10, verbose = 0)

y_pred = np.round(model.predict(X_test))  # Redondeamos pues obtenemos un número entre 0 y 1

scores = model.evaluate(X_test, y_test)

print(model.metrics_names[1], scores[1])



resumenMatrizPrecisiones(instancia_red, X_test, y_test, y)



#Ejercicio 2



import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import math
import random
from sklearn.preprocessing import MinMaxScaler
from   sklearn.datasets import make_blobs
# Import the dendrogram function and the ward, single, complete, average, linkage and fcluster clustering function from SciPy
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
from scipy.spatial.distance import pdist
from sklearn.utils.multiclass import unique_labels
from keras.models import Sequential      
from keras.layers import Dense
from keras.layers import Reshape
    
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VII Lecture")

pd.set_option('display.max_rows', 1000)

datos_caras = pd.read_csv('8carasFamosas.csv',delimiter=';',decimal=".",index_col=0)


print(datos_caras.head())


def centroide(num_cluster, datos, clusters):
  ind = clusters == num_cluster
  return(pd.DataFrame(datos[ind].mean()).T)

    
def plot_image(valor_cara, titulo = None, filas = 62, cols = 47):
    image = np.array(list(reversed(valor_cara)))
    image = pd.to_numeric(image, errors = 'coerce')
    image = image.reshape(filas, cols)
    plt.imshow(image, cmap = "pink")
    ejes = plt.gca()
    ejes.axes.get_xaxis().set_visible(False)
    ejes.axes.get_yaxis().set_visible(False)
    if titulo is not None:
        plt.title(titulo)
        
plot_image(datos_caras.iloc[0, range(2914)], datos_caras.iloc[0, range(2914)])

       

for i in range(1, 9):
    plt.subplot(2, 4, i)
    cara = random.randint(0, datos_caras.shape[0])
    plot_image(datos_caras.iloc[cara, range(2914)], datos_caras.iloc[cara, range(2914)])

    
X = datos_caras.iloc[:, :-1]

print(X.head())
    
y = datos_caras.iloc[:,-1]

print(y.head())


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)


#2b

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

#Mejor resultado 61 * 61 = 0.805

instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[61, 61])

instancia_red.fit(X_train,y_train)

print("Precisión en Testing: {:.3f}".format(instancia_red.score(X_test, y_test)))

"""
values = {"value" : 0, "i" : 0, "j" : 0}
 
for i in range(1, 100):
    for j in range(1, 100):
        instancia_red = MLPClassifier(solver='lbfgs', random_state=0,hidden_layer_sizes=[i, j])
        instancia_red.fit(X_train,y_train)
        print(i, j)
        newVal = instancia_red.score(X_test, y_test)
        if(newVal > values["value"]):
            values["value"] = newVal
            values["i"] = i
            values["j"] = j
            print("Precisión en Testing: {:.3f}".format(newVal))
  
print(values["value"])

"""


#Version usando keras


#Volvemos a sacar las variables

X = datos_caras.iloc[:, :-1]

print(X.head())
    
y = datos_caras.iloc[:,-1]

print(y.head())

#Disyuntivo en variable a predecir
dummy_y = pd.get_dummies(y)


scaler = MinMaxScaler(feature_range = (0, 1))
scaled_X  = pd.DataFrame(scaler.fit_transform(X), columns = list(X))

X_train, X_test, y_train, y_test = train_test_split(scaled_X, dummy_y, train_size = 0.8, random_state = 0)

print(X_train.head())

print(X_test.head())

print(y_train.head())

print(y_test.head())


model = Sequential()
model.add(Dense(50, input_dim = 2913, activation = 'relu'))  # Agregamos primera capa oculta con 10 neuronas
model.add(Dense(8, activation = 'softmax')) # Agregamos capa output con 3 neuronas

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

print(model.summary())


model.fit(X_train, y_train, epochs = 100, batch_size = 10, verbose = 0)

y_pred = model.predict(X_test)
# Convertimos a columna
y_test_class = np.argmax(np.asanyarray(y_test), axis = 1)  # Convertimos a array
y_pred_class = np.argmax(y_pred, axis = 1)


scores = model.evaluate(X_test, y_test)

print(model.metrics_names[1], scores[1])



#Ejercicio 4
u = np.arange(0, 1.1, 0.1)

v = np.arange(-1, 0, 0.1)

v = np.append(v, u)

w = np.empty(3) 
w.fill(0)

print(u)
print(v)
print(w)


#I(t)
def identity(value, compare):
    return 1 if value >= compare else 0