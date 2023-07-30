"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma 
de los n primeros enteros positivos puede ser calculada de la siguiente forma:

                    suma = n(n+1)/2
"""
trigger = True
while(trigger == True):
    num = int(input("Ingresa un numero entero positivo: "))

    if (num > 0):
        suma = num * (num + 1)/2
        print("La suma desde 1 hasta " + str(num) + " es: " + str(suma))
        trigger = False
    else:
        trigger = True