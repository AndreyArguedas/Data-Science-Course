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


"""
En el primer cluster observamos como la mayoría de paises durante ese tiempo
importaron poco producto, Panama, El Salvador y CR importan niveles similares
mientras que Nicaragua y Honduras lo hacen en menor cantidad.

En el segundo cluster vemos como Panama, Guatemala y El Salvador comenzaron
a importar mucho más, todos los paises en general crecieron las importaciones
excepto CR.

En el tercer cluster vemos como los paises del triangulo norte (Guatemala
Honduras, El Salvador) bajaron sus importaciones mientras que la parte sur
de CentroAmerica (Costa Rica, Nicaragua, Panama), crecieron sus importaciones
"""

plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos.columns)
open_close_plot()

"""
En el grafico de radar podemos observar como los paises vecinos tienden
a tomar decisiones de importaciones similares a sus vecinos, ejemplo, el cluster 2
nos muestra que en un mismo periodo de tiempo Nicaragua,Panama y CR importaron mas,
mientras que en el cluster 1 vemos lo mismo para los paises de la zona norte
de centroamerica.

En el cluster 0 vemos como todos los paises tomaban decisiones similares e
importaban muy poco de Mexico.
"""

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

grupos = fcluster(linkage(pdist(datos), method = 'ward', metric='binary'), 3, criterion = 'maxclust')
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

"""
En el cluster 0 podemos observar los altos niveles de alcohol, podemos ademas ver
el alto porcentaje del comportamiento de tipo A y la adiposity, podemos ver que la
obesidad es similar a los demas clusters y el consumo de tabaco esta presente.

En el cluster 1 podemos observar que el grupo es de menor de edad, consumen
menos alcohol y practicamente no consumen tabaco, los demas indicadores se encuentran
muy similar a los demas clusters

En el cluster 2 vemos indicadores muy promedio pero con poco consumo de alcohol

Como conclusion podemos ver que a pesar de la edad y bajos consumos de alcohol
y tabaco los indicadores de obesidad, typeA, adiposity y ldl se encuentran similar
entre grupos
"""

plt.figure(1, figsize = (10, 10))
radar_plot(centros, datos.columns)
open_close_plot()

"""
Podemos ver como a mayor edad tambien hay mayor consumo de tabaco y alcohol,
ademas vemos una relacion entre el ldl y adiposity, encontramos relaciones negativas
entre el consumo de tabaco y la obesidad asi como el comportamiento type A y la edad
"""   

#2.d

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

del datos['Anno']

kmeans = KMeans(n_clusters=3,n_init=10,max_iter=500)

kmeans.fit(datos)

print(kmeans.predict(datos))


centros = np.array(kmeans.cluster_centers_)
print(centros) 

#3f

plt.figure(1, figsize = (12, 8))
bar_plot(centros, datos.columns)
open_close_plot()

"""
Podemos observar como cuando la velocidad del viento sube la
concentracion Particula disminuye
"""

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
        
class Clusters(Exploratorio):
    def __init__(self, df = pd.DataFrame(), n_clusters = 1):
        super().__init__(df)
        self.__n_clusters = n_clusters
        
    @property
    def n_clusters(self):
        return self.__n_clusters 
    @n_clusters.setter
    def n_clusters(self, n_clusters):
        self.__n_clusters  = n_clusters
    
    def __str__(self):
        return super().__str__()
    
    def analisis(self):
        super().analisis()
        
    def graficar_barras(self, array):
        plt.figure(1, figsize = (12, 8))
        bar_plot(array, self.df.columns)
        open_close_plot()
    
    def graficar_radar(self, array):
        plt.figure(1, figsize = (12, 8))
        radar_plot(array, self.df.columns)
        open_close_plot()
        
class Jerarquico(Clusters):
    def __init__(self, df = pd.DataFrame(), n_clusters = 1):
        super().__init__(df, n_clusters)
    
    def __str__(self):
        return super().__str__()
    
    def analisis(self):
        grupos = fcluster(linkage(pdist(self.df), method = 'ward', metric='euclidean'), 3, criterion = 'maxclust')
        grupos = grupos-1 # Se resta 1 para que los clústeres se enumeren de 0 a (K-1), como usualmente lo hace Python
        arrays = []
        for i in range(0, self.n_clusters):
            arrays.append(centroide(i, datos, grupos))
        centros = np.array(pd.concat(arrays))
        super().graficar_barras(centros)
        super().graficar_radar(centros)
        
class Kmeans(Clusters):
    def __init__(self, df = pd.DataFrame(), n_clusters = 1):
        super().__init__(df, n_clusters)
    
    def __str__(self):
        return super().__str__()
    
    def analisis(self):
        kmedias = KMeans(self.n_clusters)
        kmedias.fit(self.df)
        centros = np.array(kmedias.cluster_centers_)
        super().graficar_barras(centros)
        super().graficar_radar(centros)
        

    
#Test
        
import os
import pandas as pd

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/VI Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
        
exp = Exploratorio(datos.loc[:, ~datos.columns.isin(['famhist', 'chd'])])

print("==========EXPLORATORIO==========")

exp.analisis()


print("==========JERARQUICO==========")

jer = Jerarquico(datos.loc[:, ~datos.columns.isin(['famhist', 'chd'])], 3)

jer.analisis()

print("==========K-MEANS==========")

km = Kmeans(datos.loc[:, ~datos.columns.isin(['famhist', 'chd'])], 3)

km.analisis()