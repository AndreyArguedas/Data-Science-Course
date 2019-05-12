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