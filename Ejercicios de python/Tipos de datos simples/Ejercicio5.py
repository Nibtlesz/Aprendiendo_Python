"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""

hours = input("Ingresa las horas trabajadas: ")
cost = input("Ingresa el costo por hora: ")
total = float(hours) * float(cost)

print("Paga correspondiente: $" + str(total))