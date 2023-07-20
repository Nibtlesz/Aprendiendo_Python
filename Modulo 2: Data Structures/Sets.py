#Sets
#Son como una especie de listas y arreglos solo que con un input diferente.
#Son listas desordenadas, que solo contienen elementos unicos, al momento de crear un SET los elementos repetidos se unifican

Set1 = {"pop", "metal", "rock", "hardcore", "metal", "disco", "metal"}

print(Set1)

#Tambien se pueden convertir List a Set con la funciòn set()
albumList = ["Linkin Park", "What ive done?", "What ive done?", 2006]

print("Lista antes del SET(): " + str(albumList))

albumSet = set(albumList)

print("Lista despues del SET(): " + str(albumSet))

#Los SET puede verse como universos (mejor ejemplificados en un diagrama de Venn) que contienen diversos elementos dentro
#Para el universor A se puede ocupar la función add() el cual añadirá nuevos elementos al universo A, pero jamas duplicará dichos elementos

A = {"metallica","AC/DC", "Triller"}
print("Universo A: " + str(A)) #Universo A antes de añadir elementos
A.add("NSYNC")
A.add("NSYNC")
print("Universo A: " + str(A))#Universo A despues de añadir elementos

#Tambien podemos usar la función remove() para retirar elementos dentro del universo A
A.remove('NSYNC')
print("Universo A: " + str(A))

#Con el metodo in podemos verificar si el elemento se encuentra dentro de nuestro SET, esto retornara un valor booleano
searchElements = "metallica" in A
print("Elemento 'metallica' se encuentra en la lista?: " + str(searchElements))
searchElements = "Who" in A
print("Elemento 'Who' se encuentra en la lista?: " + str(searchElements))

#Para ocupar matematicas discretas y encontrar la intersección de dos sets se ocupa el ampersand &
albumSet1 = {"Sleep On A Dream", "Fragmentos", "Ecos", 2023}
albumSet2 = {"Sleep On A Dream", "Fragmentos", "Voces", 2023}

albumSet3 = albumSet1 & albumSet2
print("Set 1: " + str(albumSet1))
print("Set 2: " + str(albumSet2))
print("interseccion: " + str(albumSet3))

#Tambien podemos representar la Union de los dos sets con la función union()
print("union:" + str(albumSet1.union(albumSet2)))

#Con la funciòn issubset() podemos saber si todos los elementos de un set se encuentra en el otro, este retornarà un valor booleano
U = {'A', 'E'}
S = {'A', 'B', 'C', 'D', 'E'}
print("Existen elementos que se intersectan? " + str(U.issubset(S)))