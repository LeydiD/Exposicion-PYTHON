class Producto:
    
    def __init__(self, id, descripcion, costo):
        self.id= id
        self.descripcion= descripcion
        self.costo= costo
        
    def crear_etiqueta(self):
        return " %s \n %s \n %0.2f \n" %(self.id, self.descripcion, self.costo)
    
class Perecedero(Producto): #El producto entre parentesis indica que se esta heredando

    def __init__(self, id, descripcion, costo, fecha_caducidad):
        super().__init__(id, descripcion, costo)
        self.fecha_caducidad= fecha_caducidad
        
    def crear_etiqueta(self):
        return super().crear_etiqueta() + " %s \n" % self.fecha_caducidad
        

class Electronico(Producto):
    
    def __init__(self, id, descripcion, costo,marca):
        super().__init__(id, descripcion,costo)
        self.marca= marca
        
    '''def crear_etiqueta(self):
        return super().crear_etiqueta() + " %s \n" % self.marca '''
    
    
producto= Producto("g", "Generico", 100.10)
per= Perecedero("p", "Tomate", 2000, "01/01/2022")
ele= Electronico("e", "Lavadora", 300, "Samsung")

#print(producto.crear_etiqueta())
#print(per.crear_etiqueta())
#print(ele.crear_etiqueta())

objetos = (producto, per, ele)

for objeto in objetos:
    print(objeto.crear_etiqueta() , type(objeto))
