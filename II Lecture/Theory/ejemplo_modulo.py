#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:28:17 2018

@author: oldemarrodriguez
"""

import numpy as np

# Encuentra el mÃ¡ximo de un DataFrame
def maximo(DF):
  n = DF.shape[0]
  m = DF.shape[1]
  max = DF.iloc[0,0]
  for i in range(n):
    for j in range(m):
      if DF.iloc[i,j] > max:
        max = DF.iloc[i,j]
  return max


# Ejemplo: Retornando una lista de valores
# La siguiente funciÃ³n recibe un DataFrame (DF) y retorna en un diccionario el valor mÃ­mimo, 
# el mÃ¡ximo, la cantidad de ceros y la cantidad de nÃºmeros pares que contiene el dataFrame:
def valores(DF):
  n = DF.shape[0]
  m = DF.shape[1]
  min = DF.iloc[0,0]
  max = DF.iloc[0,0]
  total_ceros = 0
  total_pares = 0
  for i in range(n):
    for j in range(m):
      if DF.iloc[i,j] > max:
        max = DF.iloc[i,j]
      if DF.iloc[i,j] < min:
        min = DF.iloc[i,j]
      if DF.iloc[i,j] == 0:
        total_ceros = total_ceros+1
      if DF.iloc[i,j] % 2 == 0:
        total_pares = total_pares+1
  return {'Maximo' : max, 'Mimimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}


# Calcula las estadÃ­sticas bÃ¡sicas en un DataFrame 
def estadisticas(DF,nc):
  media = np.mean(DF.iloc[:,nc])
  mediana = np.median(DF.iloc[:,nc])
  deviacion = np.std(DF.iloc[:,nc])
  varianza = np.var(DF.iloc[:,nc])
  maximo = np.max(DF.iloc[:,nc])
  minimo = np.min(DF.iloc[:,nc])
  return {'Variable' : DF.columns.values[nc],
          'Media' : media,
          'Mediana' : mediana,
          'DesEst' : deviacion,
          'Varianza' : varianza,
          'Maximo' : maximo,
          'Minimo' : minimo}