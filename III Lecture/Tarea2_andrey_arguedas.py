# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:07:07 2019

@author: Andrey
"""

"""
1. Se supone que una Factura que tiene los siguientes atributos: nombre cliente,
direccion cliente, monto total, porcentaje impuesto 
y total pagar = monto total +
porcentaje impuesto * monto total. 
Programe una clase al estilo propio de Python que tenga los atributos citados arriba como privados 
con sus respectivos m´etodos para obtener y
modificar dichos atributos. Adem´as debe tener un m´etodo para calcular el total pagar.
"""

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


"""
2. Programe una clase en Python que tiene tres atributos (n´umeros) A, B, y C y m´etodos para
retornar el menor, el mayor, la suma de los tres y suma cuadrados = A2 + B2 + C
"""
import math

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
        return math.pow(self.a, 2) + math.pow(self.b, 2) + math.pow(self.c, 2)
    
c1 = Conjunto(20, 3, 5)
print("El mayor es: ", c1.mayor())
print("El menor es: ", c1.menor())
print("La suma de cuadrados: ", c1.suma_cuadrados())