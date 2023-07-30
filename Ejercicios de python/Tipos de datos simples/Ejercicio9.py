"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

inversion = float(input("Ingresa la cantidad que quieres invertir: "))
interes = float(input("Ingresa el porcentaje de interès anual: "))
anios = float(input("Ingresa el numero de años: "))

capital = round(inversion * (interes / 100 + 1) ** 2, 2)
print("El capital final es: " + str(capital))