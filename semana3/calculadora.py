#calculadora que realizara operaciones matematicas
#se definen las funciones poara cada operacion
#una funcion que imprima un resultado#capturar datos para realizar las operaciones (entradas de usuario) input
#operaciones matematicas
#al utilizar funciones

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2    

def dividir(num1, num2):
    return num1 / num2 

def imprimir_resultado(resultado):
    print(f"El resultado de la operacion es: {resultado}")

print("Bienvenido a l app de calculadora")
operacion_a_realizar = input("indica la operacion matematica que deseas realizar: sumar, restar, multiplicar, dividir: ")
if(operacion_a_realizar == "sumar" or operacion_a_realizar == "restar" or operacion_a_realizar == "multiplicar" or operacion_a_realizar == "dividir"):

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))

    print(operacion_a_realizar, num1, num2)

    if (operacion_a_realizar == "sumar"):
        resultado = sumar(num1, num2)
    elif(operacion_a_realizar == "restar"):
        resultado = restar(num1, num2)
    elif(operacion_a_realizar == "multiplicar"):
        resultado = multiplicar(num1, num2)
    elif(operacion_a_realizar == "dividir"):
        resultado = dividir(num1, num2)
    else:
        print("opcion no valida")    
else:
    print("opcion no valida")
    
print(resultado)
imprimir_resultado(resultado)