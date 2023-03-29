<<<<<<< HEAD
class Coordinate:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y

class Square:
    def __init__(self,v1,v2,v3,v4):
        self.__V1=v1
        self.__V2=v2
        self.__V3=v3
        self.__V4=v4

    def __ShowCoordinateV1(self):
        print("(",self.__V1.GetX(),",",self.__V1.GetY(),")")
    def __ShowCoordinateV2(self):
        print("(",self.__V2.GetX(),",",self.__V2.GetY(),")")
    def __ShowCoordinateV3(self):
        print("(",self.__V3.GetX(),",",self.__V3.GetY(),")")
    def __ShowCoordinateV4(self):
        print("(",self.__V4.GetX(),",",self.__V4.GetY(),")")
    def ShowVertex(self):
        print("El cuadrado está compuesto por los siguientes vértices: ")
        self.__ShowCoordinateV1()
        self.__ShowCoordinateV2()
        self.__ShowCoordinateV3()
        self.__ShowCoordinateV4()

v1=Coordinate(1,1)
v2=Coordinate(4,1)
v3=Coordinate(4,4)
v4=Coordinate(1,4)

square=Square(v1,v2,v3,v4)
square.ShowVertex()



    
=======
class Coordinate:
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y

class Square:
    def __init__(self,v1,v2,v3,v4):
        self.__V1=v1
        self.__V2=v2
        self.__V3=v3
        self.__V4=v4

    def __ShowCoordinateV1(self):
        print("(",self.__V1.GetX(),",",self.__V1.GetY(),")")
    def __ShowCoordinateV2(self):
        print("(",self.__V2.GetX(),",",self.__V2.GetY(),")")
    def __ShowCoordinateV3(self):
        print("(",self.__V3.GetX(),",",self.__V3.GetY(),")")
    def __ShowCoordinateV4(self):
        print("(",self.__V4.GetX(),",",self.__V4.GetY(),")")
    def ShowVertex(self):
        print("El cuadrado está compuesto por los siguientes vértices: ")
        self.__ShowCoordinateV1()
        self.__ShowCoordinateV2()
        self.__ShowCoordinateV3()
        self.__ShowCoordinateV4()

v1=Coordinate(1,1)
v2=Coordinate(4,1)
v3=Coordinate(4,4)
v4=Coordinate(1,4)

square=Square(v1,v2,v3,v4)
square.ShowVertex()



    
>>>>>>> 5f920e28e1f0685a258c4754cf07c441d2fb57e3
