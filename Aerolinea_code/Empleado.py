import Persona

class Empleado(Persona.Persona):
    def __init__(self, cedula, nombresYApellidos, sueldo):
        super().__init__(cedula, nombresYApellidos)
        self.sueldo= sueldo
        
    def crear_etiqueta(self):
        return super().crear_etiqueta() + "Sueldo: %s" % str(self.sueldo)