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

datos = pd.read_csv('Titanic.csv',delimiter=',',decimal=".",index_col=0)
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


#1.d

import matplotlib.pyplot as plt

print("SURVIVED")

survived = pd.crosstab(index=datos["Survived"], columns="count") 

alto = [survived['count'][0], survived['count'][1]]
barras = ('NO', 'YES')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

print("******************************\n")

print("CLASS")

pclass = pd.crosstab(index=datos["Pclass"], columns="count") 

alto = [pclass['count'][0], pclass['count'][1], pclass['count'][2]]
barras = ('FIRST', 'SECOND', 'THIRD')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue', 'yellow'])
plt.xticks(y_pos, barras)


# 1.e

datos.head()
boxplots = datos.boxplot(return_type='axes')

#1.f

print("Graficos funcion de densidad para hermanos o conyugues")

densidad = datos["SibSp"].plot(kind='density')


print("Graficos funcion de densidad para hijos o padres")

densidad = datos["Parch"].plot(kind='density')


print("Graficos funcion de densidad para edades")

densidad = datos["Age"].plot(kind='density')


print("Histogramas para hermanos o conyugues")

densidad = datos["SibSp"].plot(kind='hist')

print("Histogramas para hijos o padres")

densidad = datos["Parch"].plot(kind='hist')

print("Histogramas para edades")

densidad = datos["Age"].plot(kind='hist')

import scipy.stats

"""
Para pruebas de normalidad siempre se plantean así las hipótesis.

Hipótesis:

H0: La muestra proviene de una distribución normal.

H1: La muestra no proviene de una distribución normal.

Nivel de Significancia: El nivel de significancia que se trabajará es de 0.05. Alpha=0.05

Criterio de Decisión

Si P < Alpha Se rechaza H0

Si p >= Alpha No se rechaza H0, es decir, los datos SÍ siguen la normal
"""

shapiro_resultados = scipy.stats.shapiro(datos.iloc[:,6:7])
print(shapiro_resultados)

p_value = shapiro_resultados[1]
print(p_value)

alpha = 0.05
if p_value > alpha:
    print('Sí sigue la curva Normal (No se rechaza H0)')
else:
    print('No sigue la curva Normal (Se rechaza H0)')
    
# 1.g
    
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(datos, hue='SibSp', size=2.5)

x = datos.iloc[:]["SibSp"]
y = datos.iloc[:]["Parch"]
plt.plot(x, y, 'o', color='black')

#1.h

corr = datos.corr()
print("Matriz de correlaciones \n")
print(corr)

f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)



# Ehercicio 2


# 2.a

import os
import pandas as pd
import numpy as np

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/V Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos)

# 2.c

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

print("Historial Familiar:")

print(datos['famhist'].value_counts())

print("******************************\n")

print("Coronary Heart Disease:")

print(datos['chd'].value_counts())

print("******************************\n")

print("TABLA CRUZADA - Historial familiar por Coronary Heart Disease:")

famhist_chd = pd.crosstab(index=datos["famhist"], columns=datos["chd"])
print(famhist_chd)


#2.d

import matplotlib.pyplot as plt

print("Family History")

famhist = pd.crosstab(index=datos["famhist"], columns="count") 

alto = [famhist['count'][0], famhist['count'][1]]
barras = ('PRESENT', 'ABSENT')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue'])
plt.xticks(y_pos, barras)

print("******************************\n")

print("Coronary Heart Disease")

chd = pd.crosstab(index=datos["chd"], columns="count") 

alto = [chd['count'][0], chd['count'][1]]
barras = ('Si', 'No')
y_pos = np.arange(len(barras))
plt.bar(y_pos, alto, color=['red','blue', 'yellow'])
plt.xticks(y_pos, barras)

#2.e

datos.head()
boxplots = datos.boxplot(return_type='axes')

#2.f

print("Graficos funcion de densidad para tobacco")

densidad = datos["tobacco"].plot(kind='density')

print("Graficos funcion de densidad para low densiity lipoprotein ")

densidad = datos["ldl"].plot(kind='density')

print("Graficos funcion de densidad para adiposity")

densidad = datos["adiposity"].plot(kind='density')

print("Graficos funcion de densidad para type A")

densidad = datos["typea"].plot(kind='density')

print("Graficos funcion de densidad para obesidad")

densidad = datos["obesity"].plot(kind='density')

print("Graficos funcion de densidad para alcohol")

densidad = datos["alcohol"].plot(kind='density')

print("Graficos funcion de densidad para edad")

densidad = datos["age"].plot(kind='density')

#Hisotgramas

print("Histogramas para tobacco")

densidad = datos["tobacco"].plot(kind='hist')

print("Histogramas para low densiity lipoprotein ")

densidad = datos["ldl"].plot(kind='hist')

print("Histogramas para adiposity")

densidad = datos["adiposity"].plot(kind='hist')

print("Histogramas para type A")

densidad = datos["typea"].plot(kind='hist')

print("Histogramas para obesidad")

densidad = datos["obesity"].plot(kind='hist')

print("Histogramas para alcohol")

densidad = datos["alcohol"].plot(kind='hist')

print("Histogramas para edad")

densidad = datos["age"].plot(kind='hist')

import scipy.stats

"""
Para pruebas de normalidad siempre se plantean así las hipótesis.

Hipótesis:

H0: La muestra proviene de una distribución normal.

H1: La muestra no proviene de una distribución normal.

Nivel de Significancia: El nivel de significancia que se trabajará es de 0.05. Alpha=0.05

Criterio de Decisión

Si P < Alpha Se rechaza H0

Si p >= Alpha No se rechaza H0, es decir, los datos SÍ siguen la normal
"""

obesity_alcohol = scipy.stats.shapiro(datos.iloc[:,6:7])
print(obesity_alcohol)

p_value = obesity_alcohol[1]
print(p_value)

alpha = 0.05
if p_value > alpha:
    print('Sí sigue la curva Normal (No se rechaza H0)')
else:
    print('No sigue la curva Normal (Se rechaza H0)')
    
# 2.g
    
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(datos, hue='obesity', size=2.5)

x = datos.iloc[:]["obesity"]

plt.plot(x,'o', color='black')

y = datos.iloc[:]["age"]

plt.plot(y,'o', color='red')

#2.h

corr = datos.corr()
print("Matriz de correlaciones \n")
print(corr)

f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)


#Ejercicio 3

import prince

import matplotlib.pyplot as plt
from prince import PCA
class ACP:
    def __init__(self, datos, n_componentes = 5): 
        self.__datos = datos
        self.__modelo = PCA(n_components = n_componentes).fit(self.__datos)
        self.__correlacion_var = self.__modelo.column_correlations(datos)
        self.__coordenadas_ind = self.__modelo.row_coordinates(datos)
        self.__contribucion_ind = self.__modelo.row_contributions(datos)
        self.__cos2_ind = self.__modelo.row_cosine_similarities(datos)
        self.__var_explicada = [x * 100 for x in self.__modelo.explained_inertia_]
    @property
    def datos(self):
        return self.__datos
    @datos.setter
    def datos(self, datos):
        self.__datos = datos
    @property
    def modelo(self):
        return self.__modelo
    @property
    def correlacion_var(self):
        return self.__correlacion_var
    @property
    def coordenadas_ind(self):
        return self.__coordenadas_ind
    @property
    def contribucion_ind(self):
        return self.__contribucion_ind
    @property
    def cos2_ind(self):
        return self.__cos2_ind
    @property
    def var_explicada(self):
        return self.__var_explicada
        self.__var_explicada = var_explicada
    def plot_plano_principal(self, ejes = [0, 1], ind_labels = True, titulo = 'Plano Principal'):
        x = self.coordenadas_ind[ejes[0]].values
        y = self.coordenadas_ind[ejes[1]].values
        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, y, color = 'gray')
        plt.title(titulo)
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.var_explicada[ejes[0]], 2)
        inercia_y = round(self.var_explicada[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        if ind_labels:
            for i, txt in enumerate(self.coordenadas_ind.index):
                plt.annotate(txt, (x[i], y[i]))
    def plot_circulo(self, ejes = [0, 1], var_labels = True, titulo = 'Círculo de Correlación'):
        cor = self.correlacion_var.iloc[:, ejes].values
        plt.style.use('seaborn-whitegrid')
        c = plt.Circle((0, 0), radius = 1, color = 'steelblue', fill = False)
        plt.gca().add_patch(c)
        plt.axis('scaled')
        plt.title(titulo)
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.var_explicada[ejes[0]], 2)
        inercia_y = round(self.var_explicada[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        for i in range(cor.shape[0]):
            plt.arrow(0, 0, cor[i, 0] * 0.95, cor[i, 1] * 0.95, color = 'steelblue', 
                      alpha = 0.5, head_width = 0.05, head_length = 0.05)
            if var_labels:
                plt.text(cor[i, 0] * 1.05, cor[i, 1] * 1.05, self.correlacion_var.index[i], 
                         color = 'steelblue', ha = 'center', va = 'center')
    def plot_sobreposicion(self, ejes = [0, 1], ind_labels = True, 
                      var_labels = True, titulo = 'Sobreposición Plano-Círculo'):
        x = self.coordenadas_ind[ejes[0]].values
        y = self.coordenadas_ind[ejes[1]].values
        cor = self.correlacion_var.iloc[:, ejes]
        scale = min((max(x) - min(x)/(max(cor[ejes[0]]) - min(cor[ejes[0]]))), 
                    (max(y) - min(y)/(max(cor[ejes[1]]) - min(cor[ejes[1]])))) * 0.7
        cor = self.correlacion_var.iloc[:, ejes].values
        plt.style.use('seaborn-whitegrid')
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.var_explicada[ejes[0]], 2)
        inercia_y = round(self.var_explicada[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        plt.scatter(x, y, color = 'gray')
        if ind_labels:
            for i, txt in enumerate(self.coordenadas_ind.index):
                plt.annotate(txt, (x[i], y[i]))
        for i in range(cor.shape[0]):
            plt.arrow(0, 0, cor[i, 0] * scale, cor[i, 1] * scale, color = 'steelblue', 
                      alpha = 0.5, head_width = 0.05, head_length = 0.05)
            if var_labels:
                plt.text(cor[i, 0] * scale * 1.15, cor[i, 1] * scale * 1.15, 
                         self.correlacion_var.index[i], 
                         color = 'steelblue', ha = 'center', va = 'center')
                
                
import os
import pandas as pd
import numpy as np

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/V Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('ImportacionesMexico.csv',delimiter=';',decimal=",",index_col=0)
print(datos)

acp = ACP(datos,n_componentes=3)
acp.plot_plano_principal()


#3.2

acp.plot_circulo()

"""
Hay relacion positiva entre Nicaragua y Costa Rica así como entre 
los paises que son parte del triangulo del norte (Honduras, Guatemala, El Salvador)
Con esto podemos interpretar que los paises vecinos tienden a tomar decisiones de importacion
similares a sus vecinos durante mismos periodos de tiempo.
Podemos ver que Panama se matiene un poco mas al margen y no existe relacion con el
resto del istmo
"""

#3.3

acp.plot_plano_principal(ejes = [0, 1])
acp.plot_circulo()

"""
Durante los años 84 y 85 Honduras, Guatemala y El Salvador importaron más,
sin embargo durante los años desde 1981 hasta 1983 Panama, Nicaragua y Costa Rica
realizaron mayor importacion, en el segmento de 1979-1980 todos los paises importaron muy poco
"""

#3.b
acp.plot_plano_principal(ejes = [0, 2])

acp.plot_circulo()

"""
Para los años 87 y 88 observamos que Costa Rica fue el mayor importador 
y los paises del triangulo norte (Honduras, Guatemala, El Salvador)
empezaron a importar cada vez menos
"""

#Ejercicio 4


import os
import pandas as pd
import numpy as np

os.chdir("/Users/Andrey/Desktop/Data-Science-Course/V Lecture")

pd.set_option('display.max_rows', 1000)

datos = pd.read_csv('SAheart.csv',delimiter=';',decimal=".",index_col=0)
print(datos)

#4.a.1
del datos['famhist']
del datos['chd']

acp = ACP(datos,n_componentes=3)
acp.plot_plano_principal()



#4.2

acp.plot_circulo()

"""
Encontramos relacion positiva entre la obesidad y la baja densidad de lipoprotein cholesterol(ldl)
lo que quiere decir que el alcholismo puede estar provocando que baje el ldl.

Encontramos relaciones negativas del typeA con variables como alcohol, tabaco y la edad
esto quiere decir que entre las personas mas toman, alcohol, fuman o envejecen el comportamiento
de tipo A comienza a crecer un poco más.
"""

#4.3

acp.plot_plano_principal(ejes = [0, 1])
acp.plot_circulo()
