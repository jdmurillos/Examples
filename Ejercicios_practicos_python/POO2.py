class Persona:
    def __init__(self, name,lastname,age):
        self.Name=name
        self.Lastname=lastname
        self.Age=age
    
    def ShowUser(self):
        print("Name: "+self.Name)
        print("Last Name: "+self.Lastname)
        print("Age: "+self.Age)

print("ORIGINAL OBJECTS") 
p1= Persona("Mike","Futaba","28")
p1.ShowUser()

p2=Persona("Karol","Black",str(29))
p2.ShowUser()

p1.Age="30"
p1.Lastname="Wood"
p2.Age=str(30)

print("\nMODIFIED OBJECTS")
p1.ShowUser()
p2.ShowUser()

