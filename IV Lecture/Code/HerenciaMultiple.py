#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:43:07 2018

@author: oldemarrodriguez
"""

# Ejemplo Herencia MÃºltiple - VersiÃ³n 1

class ClaseBase:
    num_llamados_base = 0
    def metodo_ejemplo(self):
        print("Llamando metodo_ejemplo en clase Base")
        self.num_llamados_base += 1

class SubclaseIzquierda(ClaseBase):
    num_llamados_izquierda = 0
    def metodo_ejemplo(self):
        ClaseBase.metodo_ejemplo(self)
        print("Llamando metodo_ejemplo en SubclaseIzquierda desde SubclaseFinal")
        self.num_llamados_izquierda += 1

class SubclaseDerecha(ClaseBase):
    num_llamados_derecha = 0
    def metodo_ejemplo(self):
        ClaseBase.metodo_ejemplo(self)
        print("Llamando metodo_ejemplo en SubclaseDerecha desde SubclaseFinal")
        self.num_llamados_derecha += 1
        
class SubclaseFinal(SubclaseIzquierda, SubclaseDerecha):
    num_llamados_final = 0
    def metodo_ejemplo(self):
        SubclaseIzquierda.metodo_ejemplo(self)
        SubclaseDerecha.metodo_ejemplo(self)
        print("Llamando metodo_ejemplo desde SubclaseFinal")
        self.num_llamados_final += 1  
        
s = SubclaseFinal()
s.metodo_ejemplo()
print(s.num_llamados_final,s.num_llamados_izquierda,s.num_llamados_derecha,s.num_llamados_base)

# Ejemplo Herencia MÃºltiple - VersiÃ³n 2 - Forma correcta de hacerlo

class ClaseBase:
    num_llamados_base = 0
    def metodo_ejemplo(self):
        print("Llamando metodo_ejemplo en la clase Base")
        self.num_llamados_base += 1

class SubclaseIzquierda(ClaseBase):
    num_llamados_izquierda = 0
    def metodo_ejemplo(self):
        super().metodo_ejemplo()
        print("Llamando metodo_ejemplo en Izquierda SubclaseFinal")
        self.num_llamados_izquierda += 1

class SubclaseDerecha(ClaseBase):
    num_llamados_derecha = 0
    def metodo_ejemplo(self):
        super().metodo_ejemplo()
        print("Llamando metodo_ejemplo en Derecha SubclaseFinal")
        self.num_llamados_derecha += 1
        
class SubclaseFinal(SubclaseIzquierda, SubclaseDerecha):
    num_llamados_final = 0
    def metodo_ejemplo(self):
        super().metodo_ejemplo()
        print("Llamando metodo_ejemplo en SubclaseFinal")
        self.num_llamados_final += 1  
        
s = SubclaseFinal()
s.metodo_ejemplo()
print(s.num_llamados_final,s.num_llamados_izquierda,s.num_llamados_derecha,s.num_llamados_base)
