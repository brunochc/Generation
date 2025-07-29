#funcion :bloques de codigo encapsulado, se pueden utilizar en varias partes del programa

resultado = 2 + 2
resultado2 = 2 + 3


#-----------------
#
# funciones
# usamos def para decir a python que creare una funcion
def suma(num1, num2):
    return num1 + num2 

print(suma(3, 4))
print(suma(10, 5))
print(suma(30, 100))
# invocacion de una funcion --> se ejecuta el codigo dentro de elle, en el momento que la invoque
#print(suma()) #--> cuanto vale segun la def = 4

#def resta():
    #print(f"{3-2}")
    #return "retorno desde la funcion"

#resultado4 = resta()

#hacer una calculadora