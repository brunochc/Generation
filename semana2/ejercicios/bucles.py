# bucle for in/ nos permite ejecutar un bloque de codigo y luego lo vuelve a ejecutar

lista_de_nombres = ["ale", "luis", "alberto"]

#numeros = [1,2,3,4,5,6,7,8,9,10]
limite = int(input("hasta que numero quieres imprimiren el buzz: "))
numeros = range(1, limite +1) #imprime de la segunda pocicion que seria el numero 1 [0][1] al 10



for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizz buzz")
    elif numero % 3 == 0:  # Devuelve implicitamente true o false, si es false, reliza la siguiente comparacion, si es true, imprime el resultado
        print("es fizz")   
    elif numero % 5 == 0: # realiza el mismo paso anterior, pero no continua en la secuencia del if, sino que simplemente, al ser todas las respuestas false, actua else.
        print("buzz")
    else:
        print(numero) 