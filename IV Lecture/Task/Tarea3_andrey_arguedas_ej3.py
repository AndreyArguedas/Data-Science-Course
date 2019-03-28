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
        s = "\n***************** Fecha ************\n"
        s += "Dia:%i\nMes:%i\nAño:%i"
        s += "\n*****************************\n"
        return s % (self.dias,self.mes,self.anio)
    
    def Captura(self):
        print("**Ingrese la fecha**")
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
        
    def precioVenta(self):
        return self.precio
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = "\n***************** Producto ************\n"
        s += "Código:%i\nNombre:%s\nPrecio:%i"
        s += "\n*****************************\n"
        return s % (self.codigo,self.nombre,self.precio)
    
    def Captura(self):
        self.codigo = int(input("Digite el código del producto: "))
        self.nombre = input("Digite el nombre del producto:")
        self.precio = float(input("Digite el monto de la compra:"))
        
class ProductoMasivo(Producto):
    def __init__(self):
        super().__init__()
        """
    @property
    def pais_fabricacion(self):
        return self.__pais_fabricacion
    
    @pais_fabricacion.setter
    def pais_fabricacion(self, pais_fabricacion):
        self.__pais_fabricacion = pais_fabricacion     
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "País fabricación:%s\n"
        return s % (self.pais_fabricacion)
    
    def Captura(self):
        Producto.Captura(self)
        self.pais_fabricacion = input("Digite el país de fabricación: ")
        """
        
class ProductoNoPerecedero(Producto):
    def __init__(self, codigo = 0, nombre = "", precio = 0.0, pais_fabricacion = ""):
        super().__init__(codigo, nombre, precio)
        self.__pais_fabricacion = pais_fabricacion
    @property
    def pais_fabricacion(self):
        return self.__pais_fabricacion
    
    @pais_fabricacion.setter
    def pais_fabricacion(self, pais_fabricacion):
        self.__pais_fabricacion = pais_fabricacion
        
    def precioVenta(self):
        return self.precio + self.precio * 0.15 
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "*NO PERECEDERO*"
        s += "\nPaís fabricación:%s\nPrecio de Venta:%f\n"
        return s % (self.pais_fabricacion, self.precioVenta())
    
    def Captura(self):
        Producto.Captura(self)
        self.pais_fabricacion = input("Digite el país de fabricación: ")
        
class ProductoElectronico(ProductoNoPerecedero):
    def __init__(self, codigo = 0, nombre = "", precio = 0.0, pais_fabricacion = "", anios_garantia = 0):
        super().__init__(codigo, nombre, precio, pais_fabricacion)
        self.__anios_garantia = anios_garantia
    @property
    def anios_garantia(self):
        return self.__anios_garantia
    
    @anios_garantia.setter
    def pais_fabricacion(self, anios_garantia):
        self.__anios_garantia = anios_garantia     
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "Años de garantía:%i\n"
        return s % (self.anios_garantia)
    
    def Captura(self):
        ProductoNoPerecedero.Captura(self)
        self.anios_garantia = int(input("Digite los años de garantía: "))
        
class ProductoAbarrote(ProductoNoPerecedero, ProductoMasivo):
    def __init__(self, codigo = 0, nombre = "", precio = 0.0, pais_fabricacion = "", provedor = ""):
        super().__init__()
        self.__provedor = provedor
    @property
    def provedor(self):
        return self.__provedor
    
    @provedor.setter
    def pais_fabricacion(self, provedor):
        self.__provedor = provedor     
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "Provedor:%s\n"
        return s % (self.provedor)
    
    def Captura(self):
        super().Captura(self)
        self.provedor = input("Digite el provedor: ")
        
class ProductoPerecedero(ProductoMasivo):
    def __init__(self, peso_neto = 0.0, fecha = Fecha()):
        super().__init__()
        self.__peso_neto = peso_neto
        self.__fecha = fecha
        
    @property
    def peso_neto(self):
        return self.__peso_neto
    @property
    def fecha(self):
        return self.__fecha
    
    @peso_neto.setter
    def peso_neto(self, peso_neto):
        self.__peso_neto = peso_neto
        
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
    
    def precioVenta(self):
        return self.precio + self.precio * 0.4 
        
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = super().__str__()
        s += "*PERECEDERO*"
        s += str(self.fecha)
        s += "\nPeso Neto:%f\nPrecio de Venta:%f\n"
        return s % (self.peso_neto, self.precioVenta())
    
    def Captura(self):
        ProductoMasivo.Captura(self)
        self.fecha.Captura()
        self.peso_neto = float(input("Digite el peso_neto del producto perecedero: "))
        
class TarjetaDescuento(Base):
    def __init__(self, numero = 0, limite_credito = 0.0, pin = 0, fecha = Fecha()):
        self.__numero = numero
        self.__limite_credito = limite_credito
        self.__pin = pin
        self.__fechaVencimiento = fecha
    @property
    def numero(self):
        return self.__numero
    @property
    def limite_credito(self):
        return self.__limite_credito
    @property
    def pin(self):
        return self.__pin
    @property
    def fechaVencimiento(self):
        return self.__fechaVencimiento
    @numero.setter
    def numero(self, numero):
        self.__numero = numero     
    @limite_credito.setter
    def limite_credito(self, limite_credito):
        self.__limite_credito = limite_credito
    @pin.setter
    def pin(self, pin):
        self.__pin = pin
    @fechaVencimiento.setter
    def fechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        s = self.fechaVencimiento.__str__()
        s += "Numero:%i\nLimite Credito:%s\nPin:%i"
        return s % (self.numero,self.limite_credito,self.pin)
    
    def Captura(self):
        self.fechaVencimiento.Captura()
        self.numero = int(input("Digite el numero de la tarjeta: "))
        self.limite_credito = float(input("Digite el limite de credito:"))
        self.pin = int(input("Digite el pin de la tarjeta:"))
        

import os

class Lectura:
    def LeeDatosProducto(self):
        prod = Producto()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un producto***")
        prod.Captura()
        return prod
    def LeeDatosProductoPerecedero(self):
        prod = ProductoPerecedero()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un producto perecedero***")
        prod.Captura()
        return prod
    def LeeDatosProductoNoPerecedero(self):
        prod = ProductoNoPerecedero()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un producto no perecedero***")
        prod.Captura()
        return prod

class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        print("\n"*50)
        os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar Producto ")
        print(" [2] Insertar Producto Perecedero")
        print(" [3] Insertar Producto No Perecedero")
        print(" [5] Ver la Lista Polimorfica" )
        print(" [6] Borrar la Lista Polimorfica")
        print(" [7] Salir")
        print(" ==================================================== ")
        return input("> ")
    def __mostrarLista(self):
        print("\n"*50)
        #os.system('Clear') #os.system('cls') #en windows
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            print(15 * "*" + "\n")
    def principal(self):
        respuesta = ""
        while respuesta != "7":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosProducto())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosProductoPerecedero())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosProductoNoPerecedero())
            elif respuesta == "5":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar...")
            elif respuesta == "6":
                self.__lista.clear()

prueba = App()
prueba.principal()