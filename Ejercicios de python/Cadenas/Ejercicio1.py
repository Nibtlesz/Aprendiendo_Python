"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el 
número introducido.
"""

name = input("Ingresa tu nombre: ")
trigger = False

while(trigger == False):
    num = int(input("Ingresa un numero entero positivo: "))

    if( num > 0 ):
        trigger = True
    else:
        trigger = False

count = 0
while(count < num):
    print(name)
    count = count + 1