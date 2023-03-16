def sumar():
    sum1=float(input("Primer número: "))
    sum2=float(input("Segundo número: "))
    print("La suma es: ",sum1+sum2)

def resta():
    minuendo=float(input("Primer número: "))
    sustraendo=float(input("Segundo número: "))
    print("El resultado de la resta es: ",minuendo-sustraendo)

def multiplicar():
    multiplicando=float(input("Primer número: "))
    multiplicador=float(input("Segundo número: "))
    print("El resultado de la multipliclación es: ",multiplicando*multiplicador)

def division():
    try:
        dividendo=float(input("Primer número: "))
        divisor=float(input("Segundo número: "))
        print("El resultado de la división es: ",dividendo/divisor)
    except ZeroDivisionError:
        print("ERROR: No se puede dividir por cero")

def Factorial():
    factorial=int(input("Introduzca el número del que quiere calcular el factorial: "))
    print("El factorial de "+str(factorial)+" es: "+str(FactorialCalculo(factorial)))

def FactorialCalculo(numero):
    if numero <= 1:
        return 1
    else:
        return numero *FactorialCalculo(numero-1)
    
def Potencia():
    base=int(input("Introduzca la base de la potencia: "))
    exponente=int(input("Introduzca el exponente de la potencia: "))
    print("El valor de "+str(base)+" elevado a "+str(exponente)+" es: "+str(PotenciaCalculo(base,exponente)))

def PotenciaCalculo(base,exponente):
    if exponente <= 0:
        return 1
    else:
        return base*PotenciaCalculo(base,exponente-1)

def Calculadora():
    fin=False
    while not(fin):
        menu=int(input("Opción:"))
        if(menu==1):
            sumar()
        elif(menu==2):
            resta()
        elif(menu==3):
            multiplicar()
        elif(menu==4):
            division()
        elif(menu==5):
            Factorial()
        elif(menu==6):
            Potencia()
        elif(menu==7):
            fin=1

print("""**************Calculadora******************
Menu
1)Suma
2)Resta
3)Multiplicación
4)División
5)Factorial
6)Potencia
7)Salir""")
Calculadora()




























    



    
    












































