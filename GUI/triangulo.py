class Triangulo:
    
    def __init__(self, a, b, c):
        self.a= a
        self.b= b
        self.c= c
              
    def get_Tipo(self):
        self.tipo = "Desconocido"
        
        if self.a==self.b and self.b== self.c:
            self.tipo= "Equilátero"
            
        else:
            if self.a!=self.b and self.a!=self.c and self.b!=self.c:
                self.tipo="Escaleno"
            else:
                self.tipo= "Isósceles"
            
            if self.c**2== (self.a**2+self.b**2) or self.a**2==(self.b**2 + self.c**2)or self.b**2==(self.a**2+ self.c**2):
                self.tipo = self.tipo+ " Rectángulo" 
                
        return self.tipo
    
    # Getters (métodos GET)
    
    def get_Lado1(self):
        return self.a
    
    def get_Lado2(self):
        return self.b
    
    def get_Lado3(self):
        return self.c
    
    # Setters (métodos SET)
    
    def set_Lado1(self, a):
        self.a= a
    
    def set_Lado2(self, b):
        self.b= b
    
    def set_Lado3(self, c):
        self.c= c