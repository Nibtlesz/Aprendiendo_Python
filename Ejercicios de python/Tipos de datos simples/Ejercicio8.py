"""
Escribir un programa que pida al usuario dos números enteros y muestre por 
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números 
introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

num1 = int(input("Ingresa un primer numero entero: "))
num2 = int(input("Ingresa un segundo numero entero: "))

cociente = num1 / num2
residuo = num1 % num2

print("La división de " + str(num1) + " entre " + str(num2) + " da un cociente " + str(cociente) + " y un resto " + str(residuo) + ".")