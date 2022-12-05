import Persona

class Cliente(Persona.Persona):
    def __init__(self, cedula, nombresYApellidos, edad):
        super().__init__(cedula, nombresYApellidos)
        self._edad= edad
        
    def crear_etiqueta(self):
        return super().crear_etiqueta() + "Edad: %s" % str(self._edad)
