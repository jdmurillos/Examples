import operaciones_basicas


def Sumar():
    sum1=float(input("Primer número: "))
    sum2=float(input("Segundo número: "))
    print("La suma es: ",operaciones_basicas.Sumar(sum1,sum2))

def Restar():
    minuendo=float(input("Primer número: "))
    sustraendo=float(input("Segundo número: "))
    print("El resultado de la resta es: ",operaciones_basicas.Restar(minuendo,sustraendo))

def Multiplicar():
    multiplicando=float(input("Primer número: "))
    multiplicador=float(input("Segundo número: "))
    print("El resultado de la multipliclación es: ",operaciones_basicas.Multiplicar(multiplicando,multiplicador))

def Dividir():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    print("La división es: ",operaciones_basicas.Division(dividendo,divisor))

def Factorial():
    factorial=int(input("Introduzca el número del que quiere calcular el factorial: "))
    print("El factorial de "+str(factorial)+" es: "+str(operaciones_basicas.Factorial(factorial)))

    
def Potencia():
    base=int(input("Introduzca la base de la potencia: "))
    exponente=int(input("Introduzca el exponente de la potencia: "))
    print("El valor de "+str(base)+" elevado a "+str(exponente)+" es: "+str(operaciones_basicas.Potencia(base,exponente)))

def Calculadora():
    fin=False
    while not(fin):
        menu=int(input("Opción:"))
        if(menu==1):
            Sumar()
        elif(menu==2):
            Restar()
        elif(menu==3):
            Multiplicar()
        elif(menu==4):
            Dividir()
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

