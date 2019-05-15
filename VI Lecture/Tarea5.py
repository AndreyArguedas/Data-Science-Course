# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:51:12 2019

@author: Andrey
"""

import os
import pandas as pd

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('ImportacionesMexico.csv',delimiter=';',decimal=",",index_col=0)
print(datos)


# 1.b

#Imports Utils to find centroids and do charts

import sys

scriptpath = "Utils.py"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))

# Do the import
import Utils

ward_res = ward(datos)         #Ward
single_res = single(datos)     #Salto mínimo
complete_res = complete(datos) #Salto Máximo
average_res = average(datos)   #Promedio

print("=================================\n")
print("==============WARD===============\n")
print(ward_res)

print("=========================================\n")
print("==============SALTO MINIMO===============\n")
print(single_res)

print("=========================================\n")
print("==============SALTO MAXIMO===============\n")
print(complete_res)

print("=========================================\n")
print("================PROMEDIO=================\n")
print(average_res)

print("=========================================\n")
print("================PROMEDIO=================\n")

dendrogram(average_res,labels= datos.index.tolist())

graficar_cortes(150, 120)

print("=========================================\n")
print("==============SALTO MAXIMO===============\n")

dendrogram(complete_res,labels= datos.index.tolist())

graficar_cortes(190, 130)


print("=========================================\n")
print("==============SALTO MINIMO===============\n")

dendrogram(single_res,labels= datos.index.tolist())

graficar_cortes(115, 75)

print("=================================\n")
print("==============WARD===============\n")

dendrogram(ward_res,labels= datos.index.tolist())

graficar_cortes(250, 170)



#1.c

grupos = fcluster(linkage(pdist(datos), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
grupos = grupos-1 # Se resta 1 para que los clústeres se enumeren de 0 a (K-1), como usualmente lo hace Python
# El siguiente print es para ver en qué cluster quedó cada individuo
print(grupos)

centros = np.array(pd.concat([centroide(0, datos, grupos), 
                              centroide(1, datos, grupos),
                              centroide(2, datos, grupos)]))
print(centros)


plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos.columns)
open_close_plot()


plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos.columns)
open_close_plot()


#1.d

kmedias = KMeans(n_clusters=3)
kmedias.fit(datos)
print(kmedias.predict(datos))

centros = np.array(kmedias.cluster_centers_)
print(centros) 


plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos.columns)
open_close_plot()

plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos.columns)
open_close_plot()



#Ejercicio 2

import os
import pandas as pd

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos)

#2.b

del datos['famhist']
del datos['chd']

ward_res = ward(datos)         #Ward
single_res = single(datos)     #Salto mínimo
complete_res = complete(datos) #Salto Máximo
average_res = average(datos)   #Promedio

print("=================================\n")
print("==============WARD===============\n")
print(ward_res)

print("=========================================\n")
print("==============SALTO MINIMO===============\n")
print(single_res)

print("=========================================\n")
print("==============SALTO MAXIMO===============\n")
print(complete_res)

print("=========================================\n")
print("================PROMEDIO=================\n")
print(average_res)

print("=========================================\n")
print("================PROMEDIO=================\n")

dendrogram(average_res,labels= datos.index.tolist())

graficar_cortes(55, 45)

print("=========================================\n")
print("==============SALTO MAXIMO===============\n")

dendrogram(complete_res,labels= datos.index.tolist())

graficar_cortes(125, 100)

print("=================================\n")
print("==============WARD===============\n")

dendrogram(ward_res,labels= datos.index.tolist())

graficar_cortes(500, 350)

#2.c

kmedias = KMeans(n_clusters=3)
kmedias.fit(datos)
print(kmedias.predict(datos))


centros = np.array(kmedias.cluster_centers_)
print(centros) 


plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos.columns)
open_close_plot()

plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos.columns)
open_close_plot()

#2f

import os
import pandas as pd

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos)

datos["famhist"] = recodificar(datos["famhist"], {"Present": 1,"Absent": 0})
datos["chd"] = recodificar(datos["chd"], {"Si": 1,"No": 0})
print(datos.head())


datos_dummy = pd.get_dummies(datos)
print(datos_dummy.head())


grupos = fcluster(linkage(pdist(datos_dummy), method = 'ward', metric='binary'), 3, criterion = 'maxclust')
grupos = grupos-1 # Se resta 1 para que los clústeres se enumeren de 0 a (K-1), como usualmente lo hace Python
# El siguiente print es para ver en qué cluster quedó cada individuo
print(grupos)

centros = np.array(pd.concat([centroide(0, datos_dummy, grupos), 
                              centroide(1, datos_dummy, grupos),
                              centroide(2, datos_dummy, grupos)]))
print(centros)

plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos_dummy.columns)
open_close_plot()


plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos_dummy.columns)
open_close_plot()

#Usando Kmeans

kmedias = KMeans(n_clusters=3)
kmedias.fit(datos_dummy)
print(kmedias.predict(datos_dummy))


centros = np.array(kmedias.cluster_centers_)
print(centros) 


plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos_dummy.columns)
open_close_plot()

plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos_dummy.columns)
open_close_plot()



#Ejercicio 3

import os
import pandas as pd
import numpy as np

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('DatosBeijing.csv',delimiter=',',decimal=".",index_col=0)

print(datos.dropna().describe())

print(datos.shape)

#3.b

datos = datos.replace(to_replace='NA', value=np.nan).dropna()

print(datos.shape)


#3.c

del datos['DireccionViento']

print(datos.shape)

print(datos.head())

""" 
Se debe eliminar ya que es una variable cualitativa y no calzaría en los
metodos a utilizar (K-means y Clusting Jerarquico). La alternativa sería recodificar

"""

#3.d

# Si se ejecuta clustring jerarquico el compilador "crasheara" debido a que son
# muchos datos para utilizar este metodo


#3.e

kmeans = KMeans(n_clusters=3,n_init=10,max_iter=500)

kmeans.fit(datos)

print(kmeans.predict(datos))


centros = np.array(kmeans.cluster_centers_)
print(centros) 

#3f

plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos.columns)
open_close_plot()


#3g

Nc = range(1, 20)
kmediasList = [KMeans(n_clusters=i) for i in Nc]
varianza = [kmediasList[i].fit(datos).inertia_ for i in range(len(kmediasList))]
plt.plot(Nc,varianza,'o-')
plt.xlabel('Número de clústeres')
plt.ylabel('Varianza explicada por cada cluster (Inercia Intraclases)')
plt.title('Codo de Jambu')
plt.show()

## El codo de jambu sugiere 3 clusteres



#Ejercicio 4
from abc import  ABCMeta, abstractmethod
# Clase Abstracta, ABC Class
class Base(metaclass = ABCMeta):    
    @abstractmethod
    def __str__(self):
        pass    


class Exploratorio(Base):
    def __init__(self, df = pd.DataFrame()):
        self.__df = df
        
    @property
    def df(self):
        return self.__df 
    @df.setter
    def df(self, df):
        self.__df  = df
    
    def __str__(self):
        return str(self.df)
    
    def analisis(self):
        print("---------------HEAD------------------")
        print(self.df.head())
        print("---------------SIZE------------------")
        print(self.df.shape)
        print("---------------DESCRIBE---------------")
        print(self.df.describe())
        print("---------------PERCENTIL---------------")
        print(datos.quantile(np.array([0,.25,.50,.75,1])))
        print("---------------BOX PLOT---------------")
        boxplots = datos.boxplot(return_type='axes')
        open_close_plot()
        print("---------------DENSIDAD---------------")
        densidad = datos[datos.columns[:10]].plot(kind='density')
        open_close_plot()
        print("---------------HISTOGRAMA---------------")
        densidad = datos[datos.columns[:10]].plot(kind='hist')
        open_close_plot()
        
#Test
        
import os
import pandas as pd

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
        
exp = Exploratorio(datos.loc[:, ~datos.columns.isin(['famhist', 'chd'])])

exp.analisis()