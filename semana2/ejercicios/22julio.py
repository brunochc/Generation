#1. "Hola, mundo" y sintaxis básica
#Objetivo: Comprender la estructura mínima de un programa en Python.
#Escriba un programa que imprima en pantalla:
# "Hola, mundo"


#Escriba un segundo programa que imprima:
# "Bienvenido al mundo de Python"


print("Bienvenido al mundo de phyton")

#-------------------------------------------------------------------------
#2. Entrada de datos desde el usuario
#Objetivo: Practicar cómo un programa puede recibir datos del usuario.

#Solicite al usuario su nombre con input() y guárdelo en una variable nombre.
#Solicite su edad y guárdela en una variable edad.

#Imprima un mensaje que diga:
# "Hola, [nombre]. Tienes [edad] años."

name = input("Please, Enter your Name: ")
age = input("Enter your age: ")

print(f"Hola, {name}. Tienes {age} años.") 

#------------------------------------------------------------------
#3. Variables y tipos de datos primitivos
#Objetivo: Declarar y trabajar con variables de distintos tipos.

#Declare las siguientes variables:
#entero = 10 (int)
#decimal = 3.14 (float)
#texto = "Python" (str)
#booleano = True (bool)
#Imprima el valor de cada variable junto con su tipo usando type().

entero = 10
decimal = 3.14
texto = "phyton"
booleano = True

print("entero:", entero, "- Tipo:", type(entero))
print("decimal:", decimal, "- Tipo:", type(decimal))
print("texto:", texto, "- Tipo:", type(texto))
print("booleano:", booleano, "- Tipo:", type(booleano))


#----------------------------------------------------------
#4. Concatenación de cadenas
#Objetivo: Unir textos usando variables (identifica las variables y defínelas).
#Cree un mensaje como:


#saludo = "Hola, me llamo " + nombre + " y tengo " + edad + " años."
#Imprima el mensaje.
saludo = "Hola, me llamo " + name + " y tengo " + age + " años"
print(saludo)


#----------------------------------------------
#5. Operaciones matemáticas
#Objetivo: Usar variables numéricas en operaciones.
#Cree dos variables:
#a = 5
#b = 2.5

#Realice las siguientes operaciones y guarde el resultado en una variable e imprima los resultados:
#Suma (a + b):
#Ejemplo: resultado = a + b
#Resta (a - b)
#Multiplicación (a * b)
#División (a / b)

a = 5
b = 2.5

suma = (a + b)
resta = (a - b)
multiplicacion = (a * b)
division = (a / b)

print(suma, resta, multiplicacion, division)



#-----------------------------------------------
#6. Estructuras de datos – Listas
#Objetivo: Introducción al uso de listas.
#Cree una lista llamada frutas con 3 frutas.
#Imprima la primera fruta.
#Agregue una fruta nueva al final.

#variables 
fruta1 = "manzana"
fruta2 = "pera"
fruta3 = "naranja"

#lista que guarda las frutas
frutas = []

#añadir frutas a la lista
frutas.append(fruta1) 
frutas.append(fruta2)
frutas.append(fruta3)


# La primera fruta de la lista en Manzana
print(frutas[0])

#agregar una nueva fruta:
fruta4 = input("ingrese una nueva fruta: ")
#añadir a la lista
frutas.append(fruta4)

print(frutas)


#---------------------------------------------------------
#7. Estructuras de datos – Diccionarios (objetos)
#Objetivo: Guardar datos con claves.
#Cree un diccionario persona con los campos:

#"nombre"
#"edad"
#"ciudad"

#Imprima el valor de "ciudad".
#Cambie la edad a un nuevo valor.

# 1. Crear el diccionario persona
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

# 2. Imprimir el valor de "ciudad"
print("Ciudad:", persona["ciudad"])

# 3. Cambiar la edad a un nuevo valor
persona["edad"] = 31  # Actualizamos la edad

#Imprimir el diccionario completo para ver los cambios
print("Datos actualizados:", persona)



#8. Presentación personalizada avanzada
#Objetivo: Unir múltiples conceptos en un solo programa.
#Usando las variables (nombre, edad, ciudad), construya otra variable presentacion que diga:

#Hola, me llamo [nombre], tengo [edad] años y vivo en [ciudad]. Me gusta programar en [lenguaje].
#Imprima el mensaje.

# Definición de variables
nombre = "Ana"
edad = 25
ciudad = "Barcelona"
lenguaje = "Python"

# Creación del mensaje de presentación
presentacion = (
    f"Hola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}. "
    f"Me gusta programar en {lenguaje}."
)

# Imprimir el mensaje
print(presentacion)

