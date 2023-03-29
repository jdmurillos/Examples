class Coordinate:
    def __init__(self, x,y):
        self.X=x
        self.Y=y
    
    def ShowCoordinate (self):
        print("(",self.X,",",self.Y,")")

class Square:
    def __init__(self,v1,v2,v3,v4):
        self.V1 =v1
        self.V2 =v2
        self.V3 =v3
        self.V4 =v4

    def ShowVertex(self):
        print("El cuadrado esta compuesto por los siguientes vértices: ")
        self.V1.ShowCoordinate()
        self.V2.ShowCoordinate()
        self.V3.ShowCoordinate()
        self.V4.ShowCoordinate()

v1=Coordinate(1,1)
v2=Coordinate(4,1)
v3=Coordinate(4,4)
v4=Coordinate(1,4)

square=Square(v1,v2,v3,v4)
square.ShowVertex()



    
    