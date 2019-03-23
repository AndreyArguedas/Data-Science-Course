from Lectura import Lectura
#import os

class App:
    def __init__(self):
        self.__lista = list()
        self.__lec = Lectura()
    def __menu(self):
        print("\n"*50)
        #os.system('clear') #os.system('cls') #en windows
        print(" ==================================================== ")
        print(" [1] Insertar Persona ")
        print(" [2] Insertar Asistente")
        print(" [3] Insertar Estudiante")
        print(" [4] Insertar Estudiante de Computacion")
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
                self.__lista.append(self.__lec.LeeDatosPersona())
            elif respuesta == "2":
                self.__lista.append(self.__lec.LeeDatosAsistente())
            elif respuesta == "3":
                self.__lista.append(self.__lec.LeeDatosEstudiante())
            elif respuesta == "4":
                self.__lista.append(self.__lec.LeeDatosEstCompu())
            elif respuesta == "5":
                self.__mostrarLista()
                input("Digite cualquier tecla para continuar")
            elif respuesta == "6":
                self.__lista.clear()

prueba = App()
prueba.principal()