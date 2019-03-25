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
        print("***Bienvenido a ingresar un cliente***")
        self.nombre = input("Digite el nombre del cliente: ")
        self.direccion = input("Digite la dirección del cliente:")
        
class Compra(Base):
    def __init__(self, codigo = "", descripcion = "", montoCompra = 0):
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
        self.codigo = input("Digite el código del producto: ")
        self.descripcion = input("Digite la descripción del producto:")
        self.montoCompra = int(input("Digite el monto de la compra:"))
        
        
class Factura(Base):
    def __init__(self, porcentaje_impuesto = 0, cliente = Cliente(), compras = []):
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
        return s % (self.monto_total() ,self.porcentaje_impuesto)
    
    def Captura(self):
        self.porcentaje_impuesto = float(input("Digite el porcentaje de impuesto:"))
        cliente = Cliente()
        cliente.Captura()
        self.cliente = cliente
        print("***Bienvenido a ingresar sus compras***")
        numeroCompras = int(input("Numero de compras:"))
        for i in range(numeroCompras):
            compra = Compra()
            compra.Captura()
            self.compras.append(compra)
        
class FacturaCredito(Factura):
    def __init__(self, porcentaje_impuesto = 0, cliente = Cliente(), compras = [], plazo_credito = 0):
        super().__init__(porcentaje_impuesto, cliente, compras)
        self.__plazo_credito = plazo_credito
        
    @property
    def plazo_credito(self):
        return self.__plazo_credito
    @plazo_credito.setter
    def plazo_credito(self, plazo_credito):
        self.__plazo_credito = plazo_credito
        
    def __str__(self):
        s = super().__str__()
        s += "\nPlazo Credito:%i\n"
        return s % (self.plazo_credito)
    
    def Captura(self):
        Factura.Captura(self)
        self.porcentaje_impuesto = int(input("Digite el plazo a credito:"))
        
class FacturaContado(Factura):
    def __init__(self, porcentaje_impuesto = 0, cliente = Cliente(), compras = [], porcentaje_descuento = 0):
        super().__init__(porcentaje_impuesto, cliente, compras)
        self.__porcentaje_descuento = porcentaje_descuento
        
    @property
    def porcentaje_descuento(self):
        return self.__porcentaje_descuento
    @porcentaje_descuento.setter
    def porcentaje_descuento(self, porcentaje_descuento):
        self.__porcentaje_descuento = porcentaje_descuento
        
    def __str__(self):
        s = super().__str__()
        s += "\nPorcentaje Descuento:%1.2f\n"
        return s % (self.porcentaje_descuento)
    
    def total_pagar(self):
        return self.monto_total() + self.porcentaje_impuesto * self.monto_total() - self.porcentaje_descuento * self.monto_total()
         
    def Captura(self):
        Factura.Captura(self)
        self.porcentaje_descuento = float(input("Digite el porcentaje de descuento:"))       


"""
    Pruebas
"""

cliente1 = Cliente("Andrey Arguedas", "Heredia")

compra1 = Compra("AB15", "Producto de limpieza", 1000)
compra2 = Compra("ABF2", "Producto de cocina", 2500)
listaCompras = [compra1, compra2]
           
factura1 = Factura(0.13, cliente1, listaCompras)

print(factura1.__str__())

print("El total a pagar (con impuestos) es de: ", factura1.total_pagar())

#Otras facturas
cliente2 = Cliente("Adriana Morales", "San Jose")
cliente3 = Cliente("Liliana Espinoza", "Barva")

compra3 = Compra("FF15", "Producto de mecánica", 5000)
compra4 = Compra("CCF2", "Herramienta", 9000)
listaComprasEspeciales = [compra3, compra4]


facturaContado = FacturaContado(0.13, cliente2, listaComprasEspeciales, 0.2)
facturaCredito = FacturaCredito(0.13, cliente3, listaComprasEspeciales, 6)

print(facturaContado.__str__())
print(facturaCredito.__str__())

import os

class Lectura:
    def LeeDatosFactura(self):
        factura = Factura()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar una factura***")
        factura.Captura()
        return factura
    def LeeDatosFacturaContado(self):
        facturaContado = FacturaContado()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar una factura de contado***")
        facturaContado.Captura()
        return facturaContado
    def LeeDatosFacturaCredito(self):
        facturaCredito = FacturaCredito()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar una factura de credito***")
        facturaCredito.Captura()
        return facturaCredito


class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        print("\n"*50)
        os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar Factura ")
        print(" [2] Insertar Factura Contado")
        print(" [3] Insertar Factura Crefito")
        print(" [4] Ver la Lista Polimorfica" )
        print(" [5] Borrar la Lista Polimorfica")
        print(" [6] Salir")
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
        while respuesta != "6":
            respuesta = self.__menu()
            if respuesta == "1":
                self.__lista.append(self.__lec.LeeDatosFactura())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosFacturaContado())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosFacturaCredito())
            elif respuesta == "4":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar...")
            elif respuesta == "5":
                self.__lista.clear()

prueba = App()
prueba.principal()