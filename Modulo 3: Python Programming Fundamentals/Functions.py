#Funciones
#Las funciones reciven un input, este hace un proceso y pueden retornar un dato cambiado
#Las funciones son codigo reutilizable que podemos crear o en algunas ocasiones podemos importar
a = 1
def añadir(b):
    return a + b

c = añadir(2)
print(c)

#Funciones de Python
#Python de manera nativa ya cuenta con algunas funciones que se pueden ocupar

lista = [6,3,9,0]
print("cantidad de elementos: " + str(len(lista)))#len()

print("Sumatoria de la lista: " + str(sum(lista)))#sum()

sortedLista = sorted(lista)
print("funcion sorted: " + str(sortedLista)) #sorted()
lista.sort()
print("funcion sort: " + str(lista)) #sort()

#Las funciones sort y sorted son practicamente iguales, la funcionalidad es la misma, la unica diferencia es el metodo de llamado
#Sorted necesita una lista como input y retorna la lista ordenada.
#Sort es una función que no necesita de un input, ordena la lista original sin necesidad de retornarlo para inicializarlo en otra lista

#Haciendo nuestras propias funciones

def add1(a):
    """
    suma 1 a la variable a
    """
    b = a + 1
    return b
print(add1(5))
c = add1(10)
print(c)

"""
Multimples parametros.
Las funciones pueden recibir multiples parametros para realizar un proceso
"""

def multiplicar(a,b):
    c = a * b
    return c

print(multiplicar(3,9)) 

#Podemos crear funciones que no retorne un dato
def slipona():
    print("Sleep On A Dream")

slipona()   

"""
Podemos ocupar variables globales estas pueden funcionar dentro y fuera de las funciones donde se utilicen,
pero, las variables que se encuentren dentro de una función solo pueden ser usadas en la función, fuera de ellas
no existen.
"""

def thriller():
    Date = 1982
    return Date

Date = 2023

print(thriller())
print(Date)

def acdc(y):
    print(Rating)
    return (Rating + y)

Rating = 9
z=acdc(1)
print(Rating)

def PinkFloyd():
    global ClaimedSales #Podemos indicar dentro de las funciones que una variable es global
    ClaimedSales = "41 millones"
    return ClaimedSales

PinkFloyd()
print(ClaimedSales)