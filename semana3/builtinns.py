# los builtins son funciones incorporadas: vienen incluidas dentro del lenguaje, cuando las escribimos las llamamos
#print() es una funcion incorporada 
#Range() recibe parametros, 

numbers = [23,45,34,54,45,5465,657]

print(sum(numbers)) # sumar una lista de numeros

# calcular el numero maximo de una lista de numeros

numero_max = 0
for numero in numbers:
    if  numero > numero_max:
        numero_max = numero

print(numero_max)

#funcion incorporada para evitar lineas
print(max(numbers))