from Base import Base
from Libro import Libro

class Persona(Base):
    def __init__(self,nombre = "", edad = 0):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad  
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre     
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad  
    # Los siguientes mÃ©todos usan los set y get NO los atributos    
    def __str__(self):
        return "Persona:%s\nEdad:%i" % (self.nombre,self.edad)
    def Captura(self):
        self.nombre = input("Digite el nombre: ")
        self.edad = int(input("Digite la edad:"))
        
        
class Asistente(Persona):
    def __init__(self,nombre="",edad=0,prom=0,cur="",hA=0,carr=""):
        Persona.__init__(self,nombre,edad)
        self.__promPonderado = prom
        self.__curso = cur
        self.__horasAs = hA
        self.__carrera = carr
    @property
    def promPonderado(self):
        return self.__promPonderado
    @property
    def curso(self):
        return self.__curso 
    @property
    def horasAs(self):
        return self.__horasAs
    @property
    def carrera(self):
        return self.__carrera  
    @promPonderado.setter
    def promPonderado(self, nuevo_promPonderado):
        self.__promPonderado = nuevo_promPonderado    
    @curso.setter
    def curso(self, nuevo_curso):
        self.__curso = nuevo_curso     
    @horasAs.setter
    def horasAs(self, nueva_horasAs):
        self.__horasAs = nueva_horasAs    
    @carrera.setter
    def carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera  
    # Los siguientes mÃ©todos usan los set y get NO los atributos        
    def __str__(self):
        s ="Asistente:%s\nEdad:%i\nCarrera:%s\nHoras Asignadas:%i\nCurso:%s\nPromedio Ponderado:%s"
        return s % (self.nombre,self.edad, self.carrera, self.horasAs,self.curso,self.promPonderado)
    def Captura(self):
        Persona.Captura(self)
        self.carrera = input("Digite la carrera: ")
        self.horasAs = int(input("Digite las horas asistente:"))
        self.curso = input("Digite el curso asignado:")
        self.promPonderado = int(input("Digite el promedio ponderado:"))
        
class Estudiante(Persona):
    def __init__(self,nombre="",edad=0,examen1=0,examen2=0):
        Persona.__init__(self,nombre,edad)
        self.__examen1 = examen1
        self.__examen2 = examen2
        self.__numeroLibros = 0
        self.__libros = []
    @property
    def examen1(self):
        return self.__examen1
    @property
    def examen2(self):
        return self.__examen2 
    @property
    def numeroLibros(self):
        return self.__numeroLibros
    @property
    def libros(self):
        return self.__libros  
    @examen1.setter
    def examen1(self, nuevo_examen1):
        self.__examen1 = nuevo_examen1    
    @examen2.setter
    def examen2(self, nuevo_examen2):
        self.__examen2 = nuevo_examen2     
    @numeroLibros.setter
    def numeroLibros(self, nuevo_numeroLibros):
        self.__numeroLibros = nuevo_numeroLibros    
    @libros.setter
    def libros(self, nuevos_libros):
        self.__libros = nuevos_libros 
    # Los siguientes mÃ©todos usan los set y get NO los atributos     
    def calculaPromedio(self):
        return (self.examen1+self.examen2)/2    
    def __str__(self):
        s ="Estudiante:%s\nPromedio:%i\n=====Libros====="
        for i in range(self.numeroLibros):
            s = s +"\n"+ str(self.libros[i])
        s = s + "\n================"
        return s % (self.nombre,self.calculaPromedio())
    def Captura(self):
        Persona.Captura(self)
        self.examen1 = int(input("Nota Examen 1:"))
        self.examen2 = int(input("Nota Examen 2:"))
        self.numeroLibros = int(input("Numero de libros del estudiante:"))
        for i in range(self.numeroLibros):
            lib = Libro()
            lib.Captura()
            self.libros.append(lib)

class EstCompu(Estudiante):
    def __init__(self,nombre="",edad=0,examen1=0,examen2=0,examen3=0):
        Estudiante.__init__(self,nombre,edad,examen1,examen2)
        self.__examen3 = examen3
    @property
    def examen3(self):
        return self.__examen3        
    @examen3.setter
    def examen3(self, nuevo_examen3):
        self.__examen3 = nuevo_examen3  
    # Los siguientes mÃ©todos usan los set y get NO los atributos         
    def calculaPromedio(self):
        return (self.examen1+self.examen2+self.examen3)/3
    def __str__(self):
        s ="Estudiante ComputaciÃ³n:%s\nPromedio:%i\n=====Libros====="
        for i in range(self.numeroLibros):
            s = s +"\n"+ str(self.libros[i])
        s = s + "\n================"
        return s % (self.nombre,self.calculaPromedio())
    def Captura(self):
        Persona.Captura(self)
        self.examen1 = int(input("Nota Examen 1:"))
        self.examen2 = int(input("Nota Examen 2:"))
        self.examen3 = int(input("Nota Examen 3:"))
        self.numeroLibros = int(input("Numero de libros del estudiante:"))
        for i in range(self.numeroLibros):
            lib = Libro()
            lib.Captura()
            self.libros.append(lib)