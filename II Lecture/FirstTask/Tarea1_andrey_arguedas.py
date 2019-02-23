#!/usr/bin/env python
# coding: utf-8

# ## Tarea #1 Minería de Datos

# ## Autor : Andrey Arguedas Espinoza

# ### 1. Dado x = (3,−5,31,−1,−9,10,0,18) y dado y = (1,1,−3,1,−99,−10,10,−7) realice lo siguiente:

# #### • Introduzca x y y como listas en Python.

# In[6]:


x = [3,-5,31,-1,-9,10,0,18]
y = [1,1,-3,1,-99,-10,10,-7]

print(x)
print(y)


# #### • Calcule la media, la varianza y la desviacio´n est´andar de x.

# In[19]:


import numpy as np

media = np.mean(y)
deviacion = np.std(y)
varianza = np.var(y)

print("Media", media)
print("Deviacion estandar",deviacion)
print("Varianza", varianza)


# #### • Calcule la media, la varianza y la desviacio´n est´andar de x. 

# In[8]:


np.corrcoef(x, y)


# #### • Escriba comandos en Python para extraer las entradas 2 a la 7 de x.

# In[9]:


x[2:8]


# #### • Escriba comandos en Python para extraer las entradas de y excepto la 2 y la 7.

# In[10]:


list(filter(lambda e : y.index(e) not in (2, 7), y))


# #### • Escriba comandos en Python para extraer las entradas de y menores a -3 o mayores a 10.

# In[11]:


list(filter(lambda x: x < -3 or x > 10, y))


# #### • Escriba comandos en Python para extraer las entradas de x mayores a 0 y que sean n´umeros pares

# In[12]:


list(filter(lambda e: e > 0 and e % 2 == 0, x))


# ### 2. Usando c´odigo Python (no archivos) en un DataFrame la siguiente tabla de datos:
Peso Edad Nivel Educativo
76 25 Lic
67 23 Bach
55 19 Bach
57 18 Bach
87 57 Dr
48 13 MSc
# In[13]:


import pandas as pd

datos = {'Peso': [76, 67, 55, 57, 87, 48],
         'Edad': [25, 23, 19, 18, 57, 13],
         'Nivel Educativo': ["Lic", "Bach", "Bach", "Bach", "Dr", "MSc"]
         }
datos_pandas = pd.DataFrame(datos)
print(datos_pandas)


# ### 3. Genere una hoja de datos (“data frame”) a partir de la siguiente tabla de datos y verifique que las variables tengan el tipo de dato adecuado.
# 
# id: Identificador ´unico del estudiante.
# 
# calificacion: Nota o calificaci´on obtenida en una escala descendente de la A a la D.
# 
# duracion: Cantidad de minutos requeridos para realizar la prueba.
id calificacion duracion
1 B 64
2 C 85
3 B 76
4 A 83
5 A 80
6 A 78
7 C 68
8 B 82
9 A 89
10 B 61

# In[14]:


datos = {'calificacion': ["B", "C", "B", "A", "A", "A", "C", "B", "A", "B"],
         'duracion': [64, 85, 76, 83, 80, 78, 68, 82, 89, 61]
         }
datos_pandas = pd.DataFrame(datos)
datos_pandas.index = np.arange(1,len(datos_pandas)+1)
datos_pandas.index.name = "id"
print(datos_pandas)


# ### 4. Dado x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40) realice las siguiente operaciones:

# #### • Indique los ´ındices de los valores o entradas del vector cuya divisi´on entre 2 tiene como
# resultado 45.

# In[15]:


x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40)
indices = []
for element in x:
    if element / 2 == 45:
        indices.append(x.index(element))

indices


# #### •Indique el ´ındice del valor m´as alto del vector.

# In[16]:


x.index(max(x))


# #### • Indique el resultado de la suma de los valores (entradas del vector) menores a la media del vector.
# 

# In[17]:


from functools import reduce

media = np.mean(x)

reduce((lambda x, y: x + y), list(filter(lambda e: e < media, x)))


# #### • Utilizando el operador l´ogico and (“y”l´ogico) indique cu´ales los valores del vector que son mayores a la media del vector y que sean divisibles entre 2.
# 

# In[20]:


media = np.mean(x)

list(filter(lambda e: e > media and e % 2 == 0, x))


# ### 5. Para las variables almacenadas de la siguiente forma v1 = (2,7,6,4,52), v2 = (7,5,7,0,1)) y v3 = (2,4,3,5,6) usando el comando sum calcule la sumatoria de cada una de esas variables. Repita lo anterior usando un for(...).

# In[23]:


v1 = (2,7,6,4,52)
v2 = (7,5,7,0,1)
v3 = (2,4,3,5,6)

print("Sum v1", sum(v1))

print("Sum v2", sum(v2))

print("Sum v3", sum(v3))

def suma(v):
    acum = 0
    for i in v:
        acum += i
    return acum

print("--------------------")

print("Suma v1", suma(v1))

print("Suma v2", suma(v2))

print("Suma v3", suma(v3))


# ### 6. Dado x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40) construya una lista llamada lista1 que tenga 3 campos Media, M´aximo y M´ınimo que tienen la media, el m´aximo y el m´ınimo respectivamente del vector x

# In[24]:


x = (24, 28, 29, 18, 95, 97, 90, 72, 87, 85, 74, 9, 40)
lista1 = [np.mean(x), max(x), min(x)]
print(lista1)


# ![image.png](attachment:image.png)

# In[25]:


import numpy as np

M1 = np.matrix([[9, 3, 4], [1, 3, -1]])
M2 = np.matrix([[91, -3], [1, 8], [-4, 5]])
A = M1 + 2 * np.transpose(M2)
print(A)


# In[ ]:




