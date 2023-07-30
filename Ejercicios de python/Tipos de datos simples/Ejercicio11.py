"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
"""

ahorro = float(input("Ingresa la cantidad a ahorrar: $"))
totalanio1 = (ahorro * 0.04) + ahorro
totalanio2 = (ahorro * 0.08) + ahorro
totalanio3 = (ahorro * 0.12) + ahorro

print("Total ahorrado el primer año: $" + str(round(totalanio1,2)))
print("Total ahorrado el segundo año: $" + str(round(totalanio2,2)))
print("Total ahorrado el tercer año: $" + str(round(totalanio3,2)))