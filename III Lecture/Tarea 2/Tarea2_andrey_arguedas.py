#!/usr/bin/env python
# coding: utf-8

# # Tarea 2

# ## Autor Andrey Arguedas Espinoza

# ### Escriba en Python con las siguientes ejercicios con al menos una prueba de ejecución de cada clase.
# 

# ![image.png](attachment:image.png)

# In[1]:


class Factura(object):
    def __init__(self, nombre_cliente, direccion_cliente, monto_total, porcentaje_impuesto):
        self.__nombre_cliente = nombre_cliente
        self.__direccion_cliente = direccion_cliente
        self.__monto_total = monto_total
        self.__porcentaje_impuesto = porcentaje_impuesto
    @property
    def nombre_cliente(self):
        return self.__nombre_cliente
    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
    
    @property
    def direccion_cliente(self):
        return self.__direccion_cliente
    @direccion_cliente.setter
    def direccion_cliente(self, direccion_cliente):
        self.__direccion_cliente = direccion_cliente

    @property
    def monto_total(self):
        return self.__monto_total
    @monto_total.setter
    def monto_total(self, monto_total):
        self.__monto_total = monto_total
        
    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto
    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, porcentaje_impuesto):
        self.__porcentaje_impuesto = porcentaje_impuesto
        
    def total_pagar(self):
        return self.monto_total + self.porcentaje_impuesto * self.monto_total

                
factura1 = Factura("Andrey Arguedas", "CR", 1500, 0.13)
print("Nombre del cliente: ", factura1.nombre_cliente)
print("Dirección del cliente: ", factura1.direccion_cliente)
print("Monto total: ", factura1.monto_total)
print("Porcentaje: ", factura1.porcentaje_impuesto)

print("El total a pagar es de: ", factura1.total_pagar())


# ### 2. Programe una clase en Python que tiene tres atributos (números) A, B, y C y métodos para retornar el menor, el mayor, la suma de los tres y suma cuadrados = A2 + B2 + C2

# In[2]:


class Conjunto(object):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, a):
        self.__a = a
    
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, c):
        self.__c = c
    
    def mayor(self):
        return max([self.a, self.b, self.c])
    
    def menor(self):
        return min([self.a, self.b, self.c])
    
    def suma_cuadrados(self):
        return self.a ** 2 + self.b ** 2 + self.c ** 2
    
c1 = Conjunto(20, 3, 5)
print("El mayor es: ", c1.mayor())
print("El menor es: ", c1.menor())
print("La suma de cuadrados: ", c1.suma_cuadrados())


# ![Captura2.PNG](attachment:Captura2.PNG)

# ![Captura3.PNG](attachment:Captura3.PNG)

# In[1]:


class Pasajero(object):
    def __init__(self, codigo, nombre, precio_boleto, porcentajeImpuesto):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_boleto = precio_boleto
        self.__porcentajeImpuesto = porcentajeImpuesto
        
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio_boleto(self):
        return self.__precio_boleto
    @precio_boleto.setter
    def precio_boleto(self, precio_boleto):
        self.__precio_boleto = precio_boleto
        
    @property
    def porcentajeImpuesto(self):
        return self.__porcentajeImpuesto
    @porcentajeImpuesto.setter
    def porcentajeImpuesto(self, porcentajeImpuesto):
        self.__porcentajeImpuesto = porcentajeImpuesto
    
    def total_pagar(self):
        return self.precio_boleto + self.porcentajeImpuesto * self.precio_boleto
    
class PasajeroFrecuente(Pasajero):
    def __init__(self, codigo, nombre, precio_boleto, porcentajeImpuesto, descuento = 0.2):
        super().__init__(codigo, nombre, precio_boleto, porcentajeImpuesto)
        self.__descuento = descuento
        
    @property
    def descuento(self):
        return self.__descuento
    @descuento.setter
    def descuento(self, descuento):
        self.__descuento = descuento
        
    def total_pagar(self):
        return self.precio_boleto + self.porcentajeImpuesto * self.precio_boleto - (self.precio_boleto * self.descuento)


class Vuelo(object):
    def __init__(self, numero, hora_salida, hora_llegada):
        self.__numero = numero
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
        
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def codigo(self, numero):
        self.__numero = numero
    
    @property
    def hora_salida(self):
        return self.__hora_salida
    @hora_salida.setter
    def hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida

    @property
    def hora_llegada(self):
        return self.__hora_llegada
    @hora_llegada.setter
    def precio_boleto(self, hora_llegada):
        self.__hora_llegada = hora_llegada
        
class VueloLocal(Vuelo):
    def __init__(self,  numero, hora_salida, hora_llegada, minimo_pasajeros, codigo, nombre, precio_boleto, porcentajeImpuesto):
        super().__init__( numero, hora_salida, hora_llegada)
        self.__minimo_pasajeros = minimo_pasajeros
        self.__pasajero_frecuente = Pasajero(codigo, nombre, precio_boleto, porcentajeImpuesto)
        
    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros
    @minimo_pasajeros.setter
    def minimo_pasajeros(self, minimo_pasajeros):
        self.__minimo_pasajeros = minimo_pasajeros
        
class VueloInternacional(Vuelo):
    def __init__(self,  numero, hora_salida, hora_llegada, pais_destino, codigo, nombre, precio_boleto, porcentajeImpuesto):
        super().__init__( numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
        self.__pasajero = PasajeroFrecuente(codigo, nombre, precio_boleto, porcentajeImpuesto)
        
    @property
    def pais_destino(self):
        return self.__pais_destino
    @pais_destino.setter
    def pais_destinos(self, pais_destino):
        self.__pais_destino = pais_destino
        
class VueloCarga(Vuelo):
    def __init__(self,  numero, hora_salida, hora_llegada, pais_destino):
        super().__init__( numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
        
    @property
    def pais_destino(self):
        return self.__pais_destino
    @pais_destino.setter
    def pais_destinos(self, pais_destino):
        self.__pais_destino = pais_destino

# Creamos los pasajeros
        
pasajero = Pasajero(1, "Andrey Arguedas", 4000, 0.13)
pasajeroFrecuente = PasajeroFrecuente(2, "Adriana Morales", 4000, 0.13)

print("El total a pagar del pasajero no frecuente es: ", pasajero.total_pagar())
print("El total a pagar del pasajero frecuente es: ", pasajeroFrecuente.total_pagar())

# Enviamos a los pasajeros a vuelos

vueloLocal = VueloLocal(1, "17:00", "21:00", 15, pasajeroFrecuente.codigo, pasajeroFrecuente.nombre, pasajeroFrecuente.precio_boleto, pasajeroFrecuente.porcentajeImpuesto)
vueloInternacional = VueloInternacional(1, "17:00", "21:00", "Costa Rica", pasajero.codigo, pasajero.nombre, pasajero.precio_boleto, pasajero.porcentajeImpuesto)


# ### 4. Agregue a la clase class mi DF() vista en clase los siguientes métodos:

# ### • Retorna la cantidad de entradas de este DataFrame que son divisibles entre 3 (Pruebe este método leyendo un archivo de datos, esto en el Script de pruebas).

# In[1]:


import pandas as pd
import numpy as np
class mi_DF():
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF  
    def maximo(self):
        max = self.DF.iloc[0,0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
        return max
    def valores(self):
        min = self.DF.iloc[0,0]
        max = self.DF.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] < min:
                    min = self.DF.iloc[i,j]
                if self.DF.iloc[i,j] == 0:
                    total_ceros = total_ceros+1
                if self.DF.iloc[i,j] % 2 == 0:
                    total_pares = total_pares+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}
    def estadisticas(self,nc):
        media = np.mean(self.DF.iloc[:,nc])
        mediana = np.median(self.DF.iloc[:,nc])
        deviacion = np.std(self.DF.iloc[:,nc])
        varianza = np.var(self.DF.iloc[:,nc])
        maximo = np.max(self.DF.iloc[:,nc])
        minimo = np.min(self.DF.iloc[:,nc])
        return {'Variable' : self.DF.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}
    def divisibles(self):
        acum = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i, j] % 3 == 0:
                    acum += 1
        return acum
    
    def covarianza_correlacion(self, c1, c2):
        covar = self.DF.iloc[:, c1].cov(self.DF.iloc[:, c2])
        corre = self.DF.iloc[:, c1].corr(self.DF.iloc[:, c2])
        c1name = self.DF.columns.values[c1]
        c2name = self.DF.columns.values[c2]
        return {"Columna 1" : c1name, "Columna 2" : c2name, "Covarianza" : covar, "Correlacion" : corre}


# In[2]:


import os
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")

datos_est = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
datos = mi_DF(datos_est)

print(datos.DF)


# In[3]:


print("Cantidad de divisibles entre 3: ", datos.divisibles())


# ![Captura4.PNG](attachment:Captura4.PNG)

# In[4]:


import os
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")

datos_est = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
datos = mi_DF(datos_est)

print("Covarianza y correlacion de Matematicas y Ciencias: ", datos.covarianza_correlacion(0, 1))


# ![optativa.PNG](attachment:optativa.PNG)

# In[2]:


import pandas as pd
import numpy as np
class mi_DF_PD(pd.DataFrame):
    @property
    def _constructor(self):
        return mi_DF_PD
    
    def maximo(self):
        max = self.iloc[0,0]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.iloc[i,j] > max:
                    max = self.iloc[i,j]
        return max
    
    def valores(self):
        min = self.iloc[0,0]
        max = self.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.iloc[i,j] > max:
                    max = self.iloc[i,j]
                if self.iloc[i,j] < min:
                    min = self.iloc[i,j]
                if self.iloc[i,j] == 0:
                    total_ceros = total_ceros+1
                if self.iloc[i,j] % 2 == 0:
                    total_pares = total_pares+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}
    
    def estadisticas(self,nc):
        media = np.mean(self.iloc[:,nc])
        mediana = np.median(self.iloc[:,nc])
        deviacion = np.std(self.iloc[:,nc])
        varianza = np.var(self.iloc[:,nc])
        maximo = np.max(self.iloc[:,nc])
        minimo = np.min(self.iloc[:,nc])
        return {'Variable' : self.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}

import os
os.chdir("/Users/Andrey/Desktop/Data-Science-Course/II Lecture/Data")

datos_est = pd.read_csv('EjemploEstudiantes.csv',delimiter=';',decimal=",",index_col=0)
datos = mi_DF_PD(datos_est)   
print(datos)
print("El máximo de la df que hereda de pandas es: ", datos.maximo())
print("Los valores que hereda de pandas es: ", datos.valores())
print("Las estadisticas son: ", datos.estadisticas(1))


# ![Captura5.PNG](attachment:Captura5.PNG)

# In[1]:


import pandas as pd
import numpy as np
class Matriz():
    def __init__(self, matriz):
        self.__num_filas = np.shape(matriz)[0]
        self.__num_columnas = np.shape(matriz)[1]
        self.__matriz = matriz
        
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def matriz(self):
        return self.__matriz
    
    def sumaTotal(self):
        acum = 0
        for i in range(self.__num_filas):
            for j in range(self.__num_columnas):
                acum += self.__matriz[i, j]
        return acum
    
    def sumaFila(self, fila):
        acum = 0
        for j in range(self.__num_columnas):
            acum += self.__matriz[fila, j]
        return acum
    
    def sumaColumna(self, col):
        acum = 0
        for i in range(self.__num_filas):
            acum += self.__matriz[i, col]
        return acum
    
    def sumaAbs(self):
        acum = 0
        for i in range(self.__num_filas):
            for j in range(self.__num_columnas):
                acum += abs(self.__matriz[i, j])
        return acum
    
    def sumaCuadrados(self):
        acum = 0
        for i in range(self.__num_filas):
            for j in range(self.__num_columnas):
                acum += self.__matriz[i, j] ** 2
        return acum

matriz = Matriz(np.matrix([[1, 2, -5], [3, 4, 3]]))

print("Suma total: ", matriz.sumaTotal())

print("Suma fila: ", matriz.sumaFila(1))

print("Suma columna: ", matriz.sumaColumna(1))

print("Suma absolutos: ", matriz.sumaAbs())

print("Suma cuadrados: ", matriz.sumaCuadrados())

