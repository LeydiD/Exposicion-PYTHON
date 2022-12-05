class Persona:
    
    def __init__(self, cedula, nombresYApellidos):
        self._cedula= cedula
        self._nombresYApellidos= nombresYApellidos
    
    def __eq__(self, otro):
        e= False
        if isinstance(otro,Persona):
            e= otro._cedula == self._cedula and otro._nombresYApellidos == self._nombresYApellidos 
        return e
    
    def crear_etiqueta(self):
        return "%s \n%s \n" %(self._nombresYApellidos, str(self._cedula))
    
    # Getters (métodos GET)
    
    def get_Cedula(self):
        return self._cedula
    
    def get_NombresYApellidos(self):
        return self._nombresYApellidos
    
    # Setters (métodos GET)
    
    def set_Cedula(self, cedula):
        self._cedula= cedula
    
    def set_NombresYApellidos(self, nombresYApellidos):
        self._nombresYApellidos= nombresYApellidos
        
    def __str__(self):
        return self._nombresYApellidos + " -- " + str(self._cedula)