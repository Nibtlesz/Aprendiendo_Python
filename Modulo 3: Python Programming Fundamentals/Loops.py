#Loops o clicos
#Como primera funciòn tenemos los rangos estos son utiles para definir el rango que se va a iterar
#En Python 3 no se va a mostrar una lista cono en Python2
a = range(0,6)
print(a)

squares = ["red", "yellow", "green", "purple","blue"]

for i in range(0, 5):
    squares[i] = "white"

print(squares)

#Tambien podemos iterar sin necesidad de colocar un rango

squares = ["red", "yellow", "green"]

for square in squares:
    print(square)

#Podemos colocar una variable i que indica el index y otra square que indica el valor de la lista, ocupamos tambien la funciòn enumerate
for i, square in enumerate(squares):
    print("index: " + str(i) + " Valor: " + str(square))

#While loops
#Los ciclos While a diferencia del For solamente se ejecutará cuando la condición se cumpla
squares = ["orange", "orange", "purple", "blue"]
newSquares = []

print("Lista de cuadros: " + str(squares))

i = 0
while( squares[i] == "orange"):
    newSquares.append(squares[i])
    i = i + 1

print("Nueva lista de cuadros: " + str(newSquares))

