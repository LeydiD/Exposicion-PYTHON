from Aerolinea import Aerolinea
from Persona import Persona
from Cliente import Cliente
from Empleado import Empleado

'''                                      Prueba                                    '''
class Prueba:
    _ar = Aerolinea()
    
    def buscar(self, p): 
        if self._ar.buscarUsuario(p) != None:
            print (p._nombresYApellidos +"  "+ str( p._cedula))
        else:
            print("No se encontró")
        
    def agregar(self,persona):
        if self._ar.agregarUsuario(persona)==True:
            print("Se agregó")
        else:
            print("No se agregó")
    
    def imprimirLista(self):
        list_usuarios = self._ar.getListaUsuarios()  
        print ("\nObjetos en la lista: \n")
        for persona in list_usuarios:
            print(persona)
            

n= int(input("Personas a agregar: "))
i=0
prueba = Prueba()
while i<n:
    cedula = int(input("Ingresa la cédula: "))
    nombre= str(input("Ingresa el nombre: "))
    persona = Persona(cedula, nombre)
    prueba.agregar(persona)
    prueba.buscar(persona)
    i+=1

pedro= Persona(2456543, "Pedro")
maria= Persona(5890093, "María")
lucia= Cliente(3456778, "Lucía", 12)
carlos= Empleado(3456789, "Carlos", 1800000)

print("")
prueba.agregar(pedro)
prueba.buscar(pedro)
print(pedro.crear_etiqueta())

print("")
prueba.buscar(maria)
prueba.agregar(maria)
print(maria.crear_etiqueta())

print("")
prueba.agregar(lucia)
print(lucia.crear_etiqueta())

print("")
prueba.agregar(carlos)
print(carlos.crear_etiqueta())

prueba.imprimirLista()


