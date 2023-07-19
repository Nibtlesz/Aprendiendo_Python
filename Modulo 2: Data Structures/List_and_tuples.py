#Tuples
#Los Tuples o arreglos, pueden contener diferente tipo de dato, string, entero o flotante todos se ordenaran apartir del inex del arreglo
Tuple1 = ('Hola', 1, 1.92)

print(Tuple1)

#Lo arreglos se pueden concatenar y estos solamente se sumaran al numero de index consecutivo

Tuple1 = Tuple1 + ("Adios", 23, 12.34)
print(Tuple1)

#Para mostrar un dato dentro del arreglo se tiene que indicar el numero del index en este ejemplo va del 0 al 5 o de manera negativa del -6 al -1

print(Tuple1[-6])#Hola
print(Tuple1[3])#Adios

#Para mostrar un rango de datos se tiene que indicar el numero de index donde se va a iniciar y el numero de elementos a mostrar
print(Tuple1[0:2])#('Hola', 1)
print(Tuple1[2:5])#(1.92,"Adios", 23)

#Con la funciòn len() podemos saber el tamaño del arreglo

print(len(Tuple1)) #6

#Tuple inmutables
#Los rreglos inmutables son cuando crears una copia del arreglo original para alterar su orden 
Ratings = (12,3,10,4,7,9,2,1,3,5,8,7)

RatingsSorted = sorted(Ratings)
print(Ratings)#Arreglo inmutable
print(RatingsSorted)#Arreglo ordenado apartir del original

#Arreglos de arreglos
#Este tipo de arreglos pueden ser bidimensionales, tridimensionales o hasta n dimensiones ya que es un arreglo de datos que contiene n cantidad de arreglos
array = (1,(2,3),(4,5,(6,7,9)))#Este es un Array de 3 elementos donde el elemento 2 y 3 con tienen 2 y 3 elementos respectivamente

print(str(array) + ' ' + 'tamaño del arreglo: ' + str(len(array)))
print(str(array[1]) + ' ' + 'tamaño del arreglo[1]: ' + str(len(array[1])))
print(str(array[2]) + ' ' + 'tamaño del arreglo[2]: ' + str(len(array[2])))
print(str(array[2][2]) + ' ' + 'tamaño del arreglo[2][2]: ' + str(len(array[2][2])))

#Listas
#Las listas son muy similares a los arreglos.
L = ["Michael Jackson", 10.1, 1982]

print("Lista: " + str(L))

#En las Listas se puede ocupar las funciones append(), extend() para añadir nuevos elementos pero funcionan un poco diferente
#extend() extiende la lista agregando el argumento en cada uno de los index de la lista
L.extend(["Hola", 2023])

print("Extend: " + str(L))

#append() añade la lista de argumentos igual que el extend(), la diferencia es que lo coloca en el siguiente index de la lista
L.append(["Adios", 1994])

print("Append: " + str(L))

#Se puede sustituir elementos dentro de la lista indicando el index que se requiere sustituir

L[0] = "Messi"
print("Elemento en la posición [0] sustituido: \n" + 'Nueva Lista: ' + str(L))

#Tambien se pueden eliminar elementos dentro de la lista con la función del()

del(L[5])

print("Elemento en la posición 5 eliminado \nNueva Lista: " + str(L))

#La función split() sirve para convertir una cadena de texto en una lista

cadena = "Hard Rock"
nuevaLista = cadena.split()
print("Cadena: " + '"' + cadena + '"\n' + "Nueva Lista: " + str(nuevaLista) )

#Tambien sle puede indicar un elemento especfico para empezar a delimitar la lista

cadena = "A,E,I,O,U"
listaVocales = cadena.split(',')
print("Cadena: " + '"' + cadena + '"\n' + "Nueva Lista: " + str(listaVocales) )

#Si referencias a la misma lista esta sera afectada en ambos lados

A = [1,2,"hola"]
B = A
B[2] = "adios"
print("Lista A: " + str(A) + "\n Lista B: " + str(B))
A[2] = "messi"
print("Lista A: " + str(A) + "\n Lista B: " + str(B))

#La mejor opcion para no alterar la lista original es clonandola, para que cada uno tenga una referencia distinta
print("Clonando")
A = [1,2,"hola"]
B = A[:] #Clonando lista
B[2] = "adios"
print("Lista A: " + str(A) + "\n Lista B: " + str(B))
A[2] = "messi"
print("Lista A: " + str(A) + "\n Lista B: " + str(B))

#Para mas ayuda con respecto a las listas puedes ocupar la funciòn help()
#help(A) #descomenta esta linea para observar la ayuda