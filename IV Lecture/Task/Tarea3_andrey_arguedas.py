# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 12:13:00 2019

@author: Andrey
"""

"""
Ejercicio 1. Ver notebook
"""

from abc import  ABCMeta, abstractmethod

# Clase Abstracta, ABC Class
class Base(metaclass = ABCMeta):    
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura(self):
        pass
    
class Factura(Base):
    def __init__(self, porcentaje_impuesto, cliente, compras = []):
        self.__porcentaje_impuesto = porcentaje_impuesto
        self.__cliente = cliente
        self.__compras = compras
        
    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto
    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, porcentaje_impuesto):
        self.__porcentaje_impuesto = porcentaje_impuesto
    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    @property
    def compras(self):
        return self.__compras
    @compras.setter
    def libros(self, compras):
        self.__compras = compras
        
    def monto_total(self):
        acum = 0
        for compra in self.compras:
            acum += compra.montoCompra
        return acum
        
    def total_pagar(self):
        return self.monto_total() + self.porcentaje_impuesto * self.monto_total()
        
    def __str__(self):
        s = "***************** Factura ************\n"
        s += "Monto total:%i\nPorcentaje Impuesto:%1.2f\n"
        s += "----Cliente----\n"
        s += str(self.cliente)
        s +="\n--------------\n"
        s += "=====Compras====="
        for compra in self.compras:
            s = s +"\n\n"+ str(compra)
        s = s + "\n================"
        return s % (self.monto_total(),self.porcentaje_impuesto)
    
    def Captura(self):
        self.monto_total = int(input("Digite el monto total: "))
        self.porcentaje_impuesto = int(input("Digite el porcentaje de impuesto:"))
        
class Cliente(Base):
    def __init__(self, nombre = "", direccion = ""):
        self.__nombre = nombre
        self.__direccion = direccion
    @property
    def nombre(self):
        return self.__nombre
    @property
    def direccion(self):
        return self.__direccion 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre     
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion= direccion  
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Persona:%s\nDirección:%s" % (self.nombre,self.direccion)
    def Captura(self):
        self.nombre = input("Digite el nombre: ")
        self.direccion = input("Digite la dirección:")
        
class Compra(Base):
    def __init__(self, codigo, descripcion = "", montoCompra = 0):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__montoCompra = montoCompra
    @property
    def codigo(self):
        return self.__codigo
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def montoCompra(self):
        return self.__montoCompra
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo     
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
    @montoCompra.setter
    def montoCompra(self, montoCompra):
        self.__montoCompra = montoCompra
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Código:%s\nDescripción:%s\nMonto Compra:%i" % (self.codigo,self.descripcion,self.montoCompra)
    def Captura(self):
        self.codigo = input("Digite el código: ")
        self.direccion = input("Digite la dirección:")
        self.montoCompra = input("Digite el monto de compra:")
        
        
        


"""
    
"""

cliente1 = Cliente("Andrey Arguedas", "Heredia")

compra1 = Compra("AB15", "Producto de limpieza", 1000)
compra2 = Compra("ABF2", "Producto de cocina", 2500)
listaCompras = [compra1, compra2]
           
factura1 = Factura(0.13, cliente1, listaCompras)

print(factura1.__str__())

print("El total a pagar (con impuestos) es de: ", factura1.total_pagar())

