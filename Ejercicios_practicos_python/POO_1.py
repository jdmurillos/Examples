class User:
    def __init__(self,nombre,apellidos,edad,peso,estatura,ciudadorigen):
        self.Nombre = nombre
        self.Apellido = apellidos
        self.Edad = edad
        self.Peso = peso
        self.Estatura = estatura
        self.Ciudadorigen = ciudadorigen
    
    def MostrarPersona(self):
        print("Nombre: "+ self.Nombre)
        print("Apellidos: "+self.Apellido)
        print("Edad: "+self.Edad)
        print("Peso: "+self.Peso)
        print("Estatura: "+self.Estatura)
        print("Ciudad de origen: "+self.Ciudadorigen)

user1= User("Ash","Ketchump","25",str(72.5),str(1.80),"Bogotá")
user1.MostrarPersona()




