"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer 
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""

clowns = float(input("Ingresa el numero de payasos vendidos: "))
dolls = float(input("Ingresa el numero de muñecas vendidas: "))

pesoClown = 112.0
pesoDoll = 75.0

total = (clowns * pesoClown) + (dolls * pesoDoll)
print("El peso total del paquete es: " + str(total) + " g")