class PublicPerson:
    def __init__(self,name,lastname,years):
        self.Name= name
        self.LastName= lastname
        self.Years= years
    
class PrivatePerson:
    def __init__(self,name,lastname,years):
        self.__Name =name
        self.__LastName =lastname
        self.__Years =years
    def GetName(self):
        return self.__Name
    def GetLastName(self):
        return self.__LastName
    def GetYears(self):
        return self.__Years
    def SetName(self,name):
        self.__Name = name
    def SetLastName(self,lastname):
        self.__LastName = lastname
    def SetYears(self,years):
        self.__Years = years

public= PublicPerson("Peter","Look",35)
private= PrivatePerson("Valery","suns",34)
print("PUBLIC PERSON")
print("Name: "+public.Name)
print("Last Name: "+public.LastName)
print("Years: "+str(public.Years))

print("PRIVATE PERSON")
print("Name: "+private.GetName())
print("Last Name: "+private.GetLastName())
print("Years old: "+str(private.GetYears()))

print("\nValues modified in both objects...")
public.LastName = "Moreno Class"
private.SetLastName ("Private Lastname")

print("PUBLIC PERSON")
print("Name: "+public.Name)
print("Last Name: "+public.LastName)
print("Years old: "+str(public.Years))

print("\nPRIVATE PERSON")
print("Name: "+private.GetName())
print("Last Name: "+private.GetLastName())
print("Years: "+str(private.GetYears()))



        

        

        
        
        