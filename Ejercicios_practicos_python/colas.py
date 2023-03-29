<<<<<<< HEAD
class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def Encolar(self,item):
        self.__items.insert(0,item)

    def Desencolar(self):
        return self.__items.pop()

    def LeerPrimerElemento(self):
        return self.__items[len(self.__items)-1]
    
    def NumeroElementos(self):
        return len(self.__items)
    
    def MostrarCola(self):
        print("Cola: ",self.__items,"<--- Primer Elemento")

def SimuladorCola():
    fin = False
    cola = Cola()
    while not (fin):
        opc = input("Opción: ") 
        if (opc == "1"):
            item=input("Introduzca elemento a encolar: ")
            cola.Encolar(item)
            print("Elemento encolado: ",item) 
        elif (opc == "2"):
            if cola.EstaVacia():
                print("La cola esta vacía, no se puede Desencolar ningun elemento")
            else:
                item = cola.LeerPrimerElemento()
                cola.Desencolar()
                print("Elemento desencolado: ",item)
        elif (opc == "3"):
            if cola.EstaVacia():
                print("La cola esta vacía, no puede leerse ningún elemento")
            else:
                print("El primer elemento es: ",cola.LeerPrimerElemento())
        elif(opc == "4"):
            print("La cola tiene: ",cola.NumeroElementos(), " elementos.")
        elif (opc == "5"):
            if cola.EstaVacia():
                print("La cola está vacía.")
            else:
                print("La cola NO está vacía.")
        elif (opc =="6"):
            cola.MostrarCola()
        elif (opc == "7"):
            fin = 1

print(""" **********Simulador de Cola **********
    Menu
    1)Encolar
    2)Desencolar
    3)Leer primer elemento
    4)Número de elementos
    5)¿Está vacía?
    6)Mostrar cola
    7)Salir """)

SimuladorCola() 
=======
class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    
    def Encolar(self,item):
        self.__items.insert(0,item)

    def Desencolar(self):
        return self.__items.pop()

    def LeerPrimerElemento(self):
        return self.__items[len(self.__items)-1]
    
    def NumeroElementos(self):
        return len(self.__items)
    
    def MostrarCola(self):
        print("Cola: ",self.__items,"<--- Primer Elemento")

def SimuladorCola():
    fin = False
    cola = Cola()
    while not (fin):
        opc = input("Opción: ") 
        if (opc == "1"):
            item=input("Introduzca elemento a encolar: ")
            cola.Encolar(item)
            print("Elemento encolado: ",item) 
        elif (opc == "2"):
            if cola.EstaVacia():
                print("La cola esta vacía, no se puede Desencolar ningun elemento")
            else:
                item = cola.LeerPrimerElemento()
                cola.Desencolar()
                print("Elemento desencolado: ",item)
        elif (opc == "3"):
            if cola.EstaVacia():
                print("La cola esta vacía, no puede leerse ningún elemento")
            else:
                print("El primer elemento es: ",cola.LeerPrimerElemento())
        elif(opc == "4"):
            print("La cola tiene: ",cola.NumeroElementos(), " elementos.")
        elif (opc == "5"):
            if cola.EstaVacia():
                print("La cola está vacía.")
            else:
                print("La cola NO está vacía.")
        elif (opc =="6"):
            cola.MostrarCola()
        elif (opc == "7"):
            fin = 1

print(""" **********Simulador de Cola **********
    Menu
    1)Encolar
    2)Desencolar
    3)Leer primer elemento
    4)Número de elementos
    5)¿Está vacía?
    6)Mostrar cola
    7)Salir """)

SimuladorCola() 
>>>>>>> 5f920e28e1f0685a258c4754cf07c441d2fb57e3
