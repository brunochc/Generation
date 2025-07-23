num = int(input("ingresa numero :"))


#modulo resto: % devuelve el resto de una division 3 % 3 =0(RESTO)
# elseif 
# el int() = convierte el input string en numero int(input("valor numerico")) = numero 
# / = division numeros entrega el resultado: 3/3 = 1


#El primer paso en esta manera de resolver el codigo, pregunta el caso en que pudiese ser ambas posibilidades, y asi no continua con pasos ejecucion y ahorraria tiempo y recurso de la maquina.
if num % 3 == 0 and num % 5 == 0:
    print("fizz buzz")
elif num % 3 == 0:  # Devuelve implicitamente true o false, si es false, reliza la siguiente comparacion, si es true, imprime el resultado
    print("es fizz")   
elif num % 5 == 0: # realiza el mismo paso anterior, pero no continua en la secuencia del if, sino que simplemente, al ser todas las respuestas false, actua else.
    print("buzz")

else:
    print(num)    