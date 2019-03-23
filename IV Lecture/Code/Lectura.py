from Personas import Persona, Estudiante, EstCompu,  Asistente
import os

class Lectura:
    def LeeDatosPersona(self):
        persona = Persona()
        os.system('clear') #os.system('cls') #en windows
        persona.Captura()
        return persona
    def LeeDatosEstudiante(self):
        estudiante = Estudiante()
        os.system('clear') #os.system('cls') #en windows
        estudiante.Captura()
        return estudiante
    def LeeDatosEstCompu(self):
        estudianteC = EstCompu()
        os.system('clear') #os.system('cls') #en windows
        estudianteC.Captura()
        return estudianteC
    def LeeDatosAsistente(self):
        asistente = Asistente()
        os.system('clear') #os.system('cls') #en windows
        asistente.Captura()
        return asistente