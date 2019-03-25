# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:04:59 2019

@author: Andrey
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
    
class Vuelo(Base):
    def __init__(self, numero = 0, hora_salida = 0, hora_llegada = 0):
        self.__numero = numero
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
        
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
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
    def hora_llegada(self, hora_llegada):
        self.__hora_llegada = hora_llegada
    
    def __str__(self):
        return "Numero de vuelo:%i\nHora de Salida:%i\nHora de Llegada:%i" % (self.numero,self.hora_salida, self.hora_llegada)
    
    def Captura(self):
        self.numero = int(input("Digite el numero del vuelo: "))
        self.hora_salida = int(input("Digite la hora de salida:"))
        self.hora_llegada = int(input("Digite la hora de llegada:"))
        
class VueloCarga(Vuelo):
    def __init__(self,  numero = 0, hora_salida = 0, hora_llegada = 0, peso_maximo = 0):
        super().__init__( numero, hora_salida, hora_llegada)
        self.__peso_maximo = peso_maximo
        
    @property
    def peso_maximo(self):
        return self.__peso_maximo
    @peso_maximo.setter
    def peso_maximo(self, peso_maximo):
        self.__peso_maximo = peso_maximo
        
    def __str__(self):
        s = super().__str__()
        s += "\nPeso Máximo:%f\n"
        return s % (self.peso_maximo)
    
    def Captura(self):
        Vuelo.Captura(self)
        self.peso_maximo = int(input("Digite el peso máximo:"))
        
class VueloComercial(Vuelo):
    def __init__(self,  numero = 0, hora_salida = 0, hora_llegada = 0, pasajeros = []):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__pasajeros = pasajeros
        
    @property
    def pasajeros(self):
        return self.__pasajeros
    @pasajeros.setter
    def peso_maximo(self, pasajeros):
        self.__pasajeros = pasajeros
    
    def monto_total_vendido(self):
        acum = 0
        for pasajero in self.pasajeros:
            acum += pasajero.total_pagar()
        return acum
    
    def __str__(self):
        s = "***************** Vuelo Comercial ************\n"
        s += "=====Pasajeros====="
        for pasajero in self.pasajeros:
            s = s +"\n\n"+ str(pasajero)
        s = s + "\n================"
        return s
    
    def Captura(self):
        numeroPasajeros = int(input("Numero de pasajeros a ingresar:"))
        for i in range(numeroPasajeros):
            pasajero = Pasajero()
            pasajero.Captura()
            self.pasajeros.append(pasajero)
        
class VueloLocal(VueloComercial):
    def __init__(self, numero = 0, hora_salida = 0, hora_llegada = 0, minimo_pasajeros = 0, porcentajeImpuesto = 0):
        super().__init__(numero, hora_salida, hora_llegada)
        self.__minimo_pasajeros = minimo_pasajeros
        
    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros
    @minimo_pasajeros.setter
    def minimo_pasajeros(self, minimo_pasajeros):
        self.__minimo_pasajeros = minimo_pasajeros
        
    def __str__(self):
        s = super().__str__()
        s += "\nMinimo de pasajeros:%i\n"
        return s % (self.minimo_pasajeros)
    
    def Captura(self):
        Vuelo.Captura(self)
        self.minimo_pasajeros = int(input("Digite el mínimo de pasajeros:"))
        
class VueloInternacional(VueloComercial):
    def __init__(self, numero = 0, hora_salida = 0, hora_llegada = 0, pais_destino = "no definido", porcentajeImpuesto = 0):
        super().__init__( numero, hora_salida, hora_llegada)
        self.__pais_destino = pais_destino
        
    @property
    def pais_destino(self):
        return self.__pais_destino
    @pais_destino.setter
    def pais_destino(self, pais_destino):
        self.__pais_destino = pais_destino
    
    def __str__(self):
        s = super().__str__()
        s += "\nPaís de destino:%s\n"
        return s % (self.pais_destino)
    
    def Captura(self):
        Vuelo.Captura(self)
        self.pais_destino = input("Digite el país de destino:")
        
class Pasajero(Base):
    def __init__(self, codigo = "", nombre = "", precio_boleto = 0, porcentajeImpuesto= 0):
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
    
    def __str__(self):
        return "Codigo:%s\nNombre:%s\nPrecio Boleto:%f\nPorcentaje Impuesto:%f" % (self.codigo,self.nombre, self.precio_boleto, self.porcentajeImpuesto)
    
    def Captura(self):
        self.codigo = input("Digite el codigo del pasajero:")
        self.nombre = input("Digite el nombre del pasajero:")
        self.precio_boleto = float(input("Digite el precio del tiquete:"))
        self.porcentajeImpuesto = float(input("Digite el porcentaje del impuesto:"))
    
class PasajeroFrecuente(Pasajero):
    def __init__(self, codigo = "", nombre = "", precio_boleto = 0, porcentajeImpuesto = 0, descuento = 0.2):
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
    
    def __str__(self):
        s = super().__str__()
        s += "\nDescuento:%s\n"
        return s % (self.descuento)
    
    def Captura(self):
        Pasajero.Captura(self)
        self.descuento = input("Digite el descuento del pasajero:")
        
import os

class Lectura:
    def LeeDatosVuelo(self):
        vuelo = Vuelo()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un vuelo***")
        vuelo.Captura()
        return vuelo
    def LeeDatosVueloCarga(self):
        vuelo = VueloCarga()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un vuelo de carga***")
        vuelo.Captura()
        return vuelo
    def LeeDatosVueloInternacional(self):
        vuelo = VueloInternacional()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un vuelo internacional***")
        vuelo.Captura()
        return vuelo
    def LeeDatosVueloLocal(self):
        vuelo = VueloLocal()
        os.system('cls') #en windows
        print("***Bienvenido a ingresar un vuelo internacional***")
        vuelo.Captura()
        return vuelo


class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        print("\n"*50)
        os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar Vuelo ")
        print(" [2] Insertar Vuelo de carga")
        print(" [3] Insertar Vuelo Internacional")
        print(" [4] Insertar Vuelo Local")
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
                self.__lista.append(self.__lec.LeeDatosVuelo())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosVueloCarga())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosVueloInternacional())
            elif respuesta == "4":
                self.__lista.append(self.__lec.LeeDatosVueloLocal())
            elif respuesta == "5":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar...")
            elif respuesta == "6":
                self.__lista.clear()

prueba = App()
prueba.principal()