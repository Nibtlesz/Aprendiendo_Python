"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un 
descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas 
que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
"""

barrasOld = float(input("Ingresa el numero de barras viejas vendidas: "))
print("Las barras del dia tiene un costo de 3.49€")
print("Al no ser pan freso se realizara un descuento de 60%")

subtotal = barrasOld * 3.49
descuento = subtotal * 0.6
total = subtotal - descuento

print("El total es: $" + str(total))