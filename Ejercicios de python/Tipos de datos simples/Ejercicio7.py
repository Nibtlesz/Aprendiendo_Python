"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

peso = float(input("Ingresa tu peso(KG): "))
estatura = float(input("Ingresa tru estatura(Mts): "))
imc = peso / (estatura ** 2)

print("Tu indice de masa corporal es: " + str(round(imc,2)))