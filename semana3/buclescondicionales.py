#Ejercicios python 

#Consejo: Revisar el concepto de split, cuidado con el tipo de datos a trabajar si es entero o string. 

#Generar una lista de números
#Pide al usuario un número n y usa un bucle while para generar una lista de los números del 1 al n.
#Ejemplo:
#Entrada: n = 5
#Salida: [1, 2, 3, 4, 5]

# pedir el numero de elementos que se desplegara
n = int(input("ingrese un numero de elementos: "))

# Donde guardare los numero de la lista ... en una lista
lista = []
#nesecito un contador, que comience en 1 y que a medida que avance hasta n, valla guardandose en la lista
i = 1

#while, mientras mi i sea menor o igual que mi n, agragaremos a la lista el valor de i, con append.

while i <= n:
    lista.append(i)
    i = i + 1

print(lista)




#Sumar elementos de una lista
#Crea un programa que use un bucle for para sumar todos los números de una lista proporcionada por el usuario.
#Ejemplo:
#Entrada: [3, 5, 7, 2]
#Salida: La suma de los elementos es: 17


#Filtrar números pares
#Solicita una lista de números al usuario y usa un bucle for para agregar solo los números pares a una nueva lista.
#Ejemplo:
#Entrada: [1, 2, 3, 4, 5, 6]
#Salida: [2, 4, 6]




#Cálculo del promedio y evaluación
#Escribe un programa que permita al usuario ingresar números (notas) hasta que escriba la palabra "fin". El programa debe calcular el promedio de las notas ingresadas. Usa un bucle while para obtener las notas y una condicional para determinar si el promedio indica que el usuario aprobó o reprobó.
#
#Condiciones:
#Si el promedio es mayor o igual a 4.0, el usuario aprueba.
#Si es menor a 4.0, el usuario reprueba.
#Ejemplo:
#
#Entrada: 5, 3, 4, fin
#
#Salida:
#El promedio es: 4.0
#¡Aprobaste!
#
#Entrada: 2, 3, fin
#
#Salida:
#El promedio es: 2.5
#Reprobaste.
#