<<<<<<< HEAD
class terreno:
    def __init__(self,base,ancho,costo):
        self.Base=base
        self.Ancho=ancho
        self.Costo=costo
    
    def MostrarCosto(self):
        print("Largo del terreno es: ",str(self.Base))
        print("Ancho del terreno es: ",str(self.Ancho))
        print("Costo del metro cuadrado: ",str(self.Costo))
        print("Costo del terreno es: ",str(self.Ancho * self.Base * self.Costo))
    

costo_total = terreno(3,4,1000)
costo_total.MostrarCosto()
=======
class terreno:
    def __init__(self,base,ancho,costo):
        self.Base=base
        self.Ancho=ancho
        self.Costo=costo
    
    def MostrarCosto(self):
        print("Largo del terreno es: ",str(self.Base))
        print("Ancho del terreno es: ",str(self.Ancho))
        print("Costo del metro cuadrado: ",str(self.Costo))
        print("Costo del terreno es: ",str(self.Ancho * self.Base * self.Costo))
    

costo_total = terreno(3,4,1000)
costo_total.MostrarCosto()
>>>>>>> 5f920e28e1f0685a258c4754cf07c441d2fb57e3
