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


"""
3. Una líınea a´erea desea implementar un sistema para el control de sus vuelos, para esto se cuenta
con la siguiente informaci´on:
    
• Se supone que un Vuelo tiene los siguientes atributos: N´umero, Hora de Salida y Hora de
Llegada.

• Un Vuelo Local (USA) tiene adem´as (respecto a un Vuelo) un N´umero M´ınimo de Pasajeros.

• Un Vuelo Internacional tiene adem´as (respecto a un Vuelo) un Pa´ıs Destino.

• Un Vuelo de Carga tiene adem´as (respecto a un Vuelo) un Peso M´aximo de carga soportado.

• Un Pasajero tiene C´odigo, Nombre, Precio Boleto, Porcentaje Impuesto y Total a Pagar
= Precio Boleto + Porcentaje Impuesto * Precio Boleto. Los pasajeros son de dos tipos:
los Pasajero Frecuente y los No Frecuentes, la diferencia es que a los pasajeros frecuentes
se les aplica un 20 % de descuento en el Total a Pagar.

• La clase Vuelo Local incluye un atributo tipo Pasajero F
"""

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

