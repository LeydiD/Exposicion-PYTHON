from Persona import Persona

class Aerolinea:
    _usuarios= []
    
    def __init__(self):
        self._usuarios= list()
    
    def buscarUsuario(self, persona):
        resultado= None
        for p in self._usuarios:
            if p.__eq__(persona):
                resultado= persona
        return resultado
    
    def agregarUsuario(self, persona):
        agregar= False
        if isinstance(persona, Persona):
            if persona not in self._usuarios:
                self._usuarios.append(persona)
                agregar= True
            else:
                agregar=False
        return agregar 
    
    def eliminarUsuario(self, persona):
        eliminar= False
        if persona in self._usuarios:
            indice= self._usuarios.index(persona)
            del self._usuarios[indice]
            eliminar=True
        return eliminar
    
    def getListaUsuarios(self):
        return self._usuarios
