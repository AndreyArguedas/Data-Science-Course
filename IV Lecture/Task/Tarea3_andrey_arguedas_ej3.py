# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:15:21 2019

@author: Andrey
"""
from abc import  ABCMeta, abstractmethod

class Base(metaclass = ABCMeta):    
    @abstractmethod
    def __str__(self):
        pass    
    @abstractmethod
    def Captura(self):
        pass
    
class Cliente(Base):
    def __init__(self, nombre = "", cedula = ""):
        self.__nombre = nombre
        self.__cedula = cedula
    @property
    def nombre(self):
        return self.__nombre
    @property
    def cedula(self):
        return self.__cedula
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre     
    @cedula.setter
    def cedula(self, cedula):
        self.__cedula= cedula  
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Cliente:%s\nCedula:%s" % (self.nombre,self.cedula)
    def Captura(self):
        self.nombre = input("Digite el nombre del cliente: ")
        self.cedula = input("Digite la cedula del cliente:")
        
class ClienteFrecuente(Cliente):
    def __init__(self, nombre = "", cedula = "", direccion = "", telefono = 0):
        super().__init__(nombre, cedula)
        self.__direccion = direccion
        self.__telefono = telefono
    @property
    def direccion(self):
        return self.__direccion
    @property
    def telefono(self):
        return self.__telefono
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion     
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono  
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "Dirección:%s\nTelefono:%i"
        return s % (self.direccion, self.telefono)
    
    def Captura(self):
        Cliente.Captura(self)
        self.direccion = input("Digite la dirección del cliente: ")
        self.telefono = input("Digite el telefono del cliente:")
        
class Fecha(Base):
    def __init__(self, dias = 1, mes = 1, anio = 1):
        self.__dias = dias
        self.__mes = mes
        self.__anio = anio
    @property
    def dias(self):
        return self.__dias
    @property
    def mes(self):
        return self.__mes
    @property
    def anio(self):
        return self.__anio
    
    @dias.setter
    def dias(self, dias):
        self.__dias = dias     
    @mes.setter
    def mes(self, mes):
        self.__mes = mes
    @anio.setter
    def anio(self, anio):
        self.__anio = anio
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Dia:%i\nMes:%i\nAño:%i" % (self.dias,self.mes,self.anio)
    def Captura(self):
        self.dias = int(input("Digite el día: "))
        self.mes = int(input("Digite el mes: "))
        self.anio = int(input("Digite el año: "))
        
class FechaCaducidad(Fecha):
    def __init__(self, dias = 1, mes = 1, anio = 1, dias_maximos = 1):
        super().__init__(dias, mes, anio)
        self.__dias_maximos = dias_maximos
    @property
    def dias_maximos(self):
        return self.__dias_maximos
    
    @dias_maximos.setter
    def dias_maximos(self, dias_maximos):
        self.__dias_maximos = dias_maximos     
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "Dias Máximos de caducidad:%s\n"
        return s % (self.dias_maximos)
    
    def Captura(self):
        Fecha.Captura(self)
        self.dias_maximos = int(input("Digite la cantidad de dias máxinos: "))
        
    
class Producto(Base):
    def __init__(self, codigo = 0, nombre = "", precio = 0.0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo     
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Código:%i\nNombre:%s\nPrecio:%i" % (self.codigo,self.nombre,self.precio)
    
    def Captura(self):
        self.codigo = int(input("Digite el código del producto: "))
        self.nombre = input("Digite el nombre del producto:")
        self.precio = float(input("Digite el monto de la compra:"))