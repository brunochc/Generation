#Ejercicios Python

#Conversión de metros a centímetros
#Escribe un programa que pida al usuario un número en metros y lo convierta a centímetros.
#Ejemplo:
#Entrada: Introduce la longitud en metros: 2
#Salida: La longitud en centímetros es: 200 cm

#entrada de datos
mts = float(input("Por favor ingrese una longitud en metros: "))

#conversion de datos, para transformar un numero en otro, como formula atematica generalmente se aplica la multiplicacion por 1 

cm = mts * 100

print(f"la longitud en centimetros de {mts} metros es: {cm} centimetros")



#Edad en el futuro
#Crea un programa que pida el nombre del usuario y su edad. Luego, calcula cuántos años tendrá en 10 años.
#Ejemplo:
#Entrada:
#Introduce tu nombre: Ana
#Introduce tu edad: 25
#Salida:
#Hola Ana, en 10 años tendrás 35 años.

name = input("Hola, ¿Cual es tu nombre?: ")
age = int(input("¿Cual es tu edad?: "))

futureage = 10 + age

print(f"{name}, tu edad en diez años sera {futureage} años.")


#Área de un rectángulo
#Pide al usuario que introduzca la base y la altura de un rectángulo, y muestra el área calculada.
#Ejemplo:
#Entrada:
#Base: 5
#Altura: 3
#Salida:
#El área del rectángulo es: 15

#ingreso de datos
base = float(input("Ingrese la medida de la base del triangulo: "))
altura = float(input("Ingrese la medida de la altura del triangulo: "))

#calculo (base*altura)/2

area = (base * altura) / 2

print(f"El area del tiangulo con base {base} cm, y altura {altura} cm, es igual a {area} cm2")




#Calculadora simple
#Pide al usuario dos números y muestra la suma, resta, multiplicación y división de esos números.
#Ejemplo:
#Entrada:
#Primer número: 8
#Segundo número: 4
#Salida:
#Suma: 12
#Resta: 4
#Multiplicación: 32
#División: 2
#
print("bienvenido a su calculadora, ingrese los datos a continuacion: ")
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

sum = num1 + num2
print(f"La suma es: {sum}")

resta = num1 - num2
print(f"La resta es: {resta}")

multi = num1 * num2
print(f"La multiplicacion es: {multi}")

div = num1 / num2
print(f"La division es: {div}")