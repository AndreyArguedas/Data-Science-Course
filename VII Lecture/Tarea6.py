# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:14:22 2019

@author: Andrey
"""

# Ejercico 2

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

#Distitnos metodos KNN

print("---------------AUTO-----------------")

instancia_knn_auto = KNeighborsClassifier(algorithm='auto')

instancia_knn_auto.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn_auto.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn_auto.score(X_test, y_test)))

print("---------------BALL TREE-----------------")

instancia_knn_ball_tree = KNeighborsClassifier(algorithm='ball_tree')

instancia_knn_ball_tree.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn_ball_tree.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn_ball_tree.score(X_test, y_test)))


print("---------------KD TREE-----------------")

instancia_knn_kd_tree = KNeighborsClassifier(algorithm='kd_tree')

instancia_knn_kd_tree.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn_kd_tree.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn_kd_tree.score(X_test, y_test)))

print("---------------BRUTE-----------------")

instancia_knn_brute = KNeighborsClassifier(algorithm='brute')

instancia_knn_brute.fit(X_train,y_train)

print("Las predicciones en Testing son: {}".format(instancia_knn_brute.predict(X_test)))

print("Precisión en Testing: {:.2f}".format(instancia_knn_brute.score(X_test, y_test)))

#4

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
    
print("Matriz de confusion y precisiones para modelo auto")

resumenMatrizPrecisiones(instancia_knn_auto, X_test, y_test, y)


print("Matriz de confusion y precisiones para modelo BALL TREE")

resumenMatrizPrecisiones(instancia_knn_ball_tree, X_test, y_test, y)


print("Matriz de confusion y precisiones para modelo KD TREE")

resumenMatrizPrecisiones(instancia_knn_kd_tree,X_test, y_test, y)

print("Matriz de confusion y precisiones para modelo BRUTE")

resumenMatrizPrecisiones(instancia_knn_brute, X_test, y_test, y)
    

    
# Ejercicio C
    
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
from   sklearn.datasets import make_blobs
# Import the dendrogram function and the ward, single, complete, average, linkage and fcluster clustering function from SciPy
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
from scipy.spatial.distance import pdist
from sklearn.utils.multiclass import unique_labels
    
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


  
    
#C.1
    
#Debemos remover la columna de Nombres
    
X = datos_caras.iloc[:, :-1]

print(X.head())
    
y = datos_caras.iloc[:,-1]

print(y.head())



ward_res = ward(X)

dendrogram(ward_res,labels= datos_caras.index.tolist())

open_close_plot()


grupos = fcluster(linkage(pdist(X), method = 'ward', metric='euclidean'), 8, criterion = 'maxclust')
grupos = grupos-1 # Se resta 1 para que los clústeres se enumeren de 0 a (K-1), como usualmente lo hace Python


centros = np.array(pd.concat([centroide(0, X, grupos),
                              centroide(1, X, grupos),
                              centroide(2, X, grupos),
                              centroide(3, X, grupos),
                              centroide(4, X, grupos),
                              centroide(5, X, grupos),
                              centroide(6, X, grupos),
                              centroide(7, X, grupos)]))

for i in range(8):
    plot_image(np.append(centros[i], 7), f'Clúster {i}')
    plt.show()

#C.2

# Primero sacar k

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VII Lecture")

pd.set_option('display.max_rows', 1000)

datos_caras = pd.read_csv('8carasFamosas.csv',delimiter=';',decimal=".",index_col=0)

predecir_col = datos_caras.iloc[:,2913:2914]

print(predecir_col.head())

X = datos_caras.iloc[:,:2913]

print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, predecir_col, train_size=0.8, random_state=0)


#C.3

cantidad = X_train.shape[0]

k = math.sqrt(cantidad)

k = math.trunc(k)

print(k)

print("---------------AUTO-----------------")

instancia_knn_auto = KNeighborsClassifier(n_neighbors = 3, algorithm='auto')

instancia_knn_auto.fit(X_train,y_train)

print("Precisión en Testing: {:.2f}".format(instancia_knn_auto.score(X_test, y_test)))

print("---------------BALL TREE-----------------")

instancia_knn_ball_tree = KNeighborsClassifier(n_neighbors = 3, algorithm='ball_tree')

instancia_knn_ball_tree.fit(X_train,y_train)


print("Precisión en Testing: {:.2f}".format(instancia_knn_ball_tree.score(X_test, y_test)))


print("---------------KD TREE-----------------")

instancia_knn_kd_tree = KNeighborsClassifier(n_neighbors = 3, algorithm='kd_tree')

instancia_knn_kd_tree.fit(X_train,y_train)


print("Precisión en Testing: {:.2f}".format(instancia_knn_kd_tree.score(X_test, y_test)))

print("---------------BRUTE-----------------")

instancia_knn_brute = KNeighborsClassifier(n_neighbors = 3, algorithm='brute')

instancia_knn_brute.fit(X_train,y_train)

print("Precisión en Testing: {:.2f}".format(instancia_knn_brute.score(X_test, y_test)))

prediccion = instancia_knn_brute.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

def plot_confusion_matrix(cm, target_names, title = 'Matriz de Confusion',cmap = None, normalize = True):
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools
    
    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy
    if cmap is None:
        cmap = plt.get_cmap('Blues')
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure(figsize = (8, 6))
    plt.imshow(cm, interpolation = 'nearest', cmap = cmap)
    plt.title(title)
    plt.colorbar()
    
    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation = 45)
        plt.yticks(tick_marks, target_names)
            
    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]), horizontalalignment="center",color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.xlabel('Precision Global={:0.4f}; Error Global={:0.4f}'.format(accuracy, misclass))
    
plot_confusion_matrix(MC, unique_labels(datos_caras['Nombres']), title = "Real",
normalize = False)

prediccion = instancia_knn_auto.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

plot_confusion_matrix(MC, unique_labels(datos_caras['Nombres']), title = "Real",
normalize = False)



prediccion = instancia_knn_ball_tree.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

plot_confusion_matrix(MC, unique_labels(datos_caras['Nombres']), title = "Real",
normalize = False)

prediccion = instancia_knn_kd_tree.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

plot_confusion_matrix(MC, unique_labels(datos_caras['Nombres']), title = "Real",
normalize = False)


prediccion = instancia_knn_brute.predict(X_test)
MC = confusion_matrix(y_test, prediccion)
print("Matriz de Confusión:\n{}".format(MC))

plot_confusion_matrix(MC, unique_labels(datos_caras['Nombres']), title = "Real",
normalize = False)