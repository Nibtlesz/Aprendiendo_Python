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



