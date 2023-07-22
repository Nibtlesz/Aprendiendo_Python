"""
En Python tenemos diferentes tipos de datos: Integer, Float, String, Boolean, List y Dictionary
Tambien tenemos Objects, que son una instancia de un tipo de dato que contienen atributos que son
caracteristicas del objeto y metodoos que son las acciones que realiza el objeto 
"""
#Atributos

class Circulo(object):
    def __init__(self, radio, color): #La función Init es un constructor donde se inicializan los atributos de la clase
        self.color = color
        self.radio = radio

    def addRadius(self, r):
        self.radio = self.radio + r 
        return self.radio

class Rectangulo(object):
    def __init__(self, color, height, width):
        self.color = color
        self.height = height
        self.width = width

redCircle = Circulo(10, 'rojo')
print("Circulo Rojo")
print("Radio: " + str(redCircle.radio))
print("Color: " + redCircle.color)

blueCircle = Circulo(50, 'Azul')
print("Circulo Azul")
print("Radio: " + str(blueCircle.radio))
blueCircle.color = "Black" #Puedes cambiar el valor del atributo aun cuando ya se habia asignado previamente
print("Color: " + blueCircle.color)

yellowRectangule = Rectangulo("Amarillo", 10, 15)
print("Rectangulo Amarillo")
print("Color: " + yellowRectangule.color)
print("Alto: " + str(yellowRectangule.height))
print("Ancho: " + str(yellowRectangule.width))

#Metodos
newRadius = redCircle.addRadius(20)
print("\nNuevo radio circulo rojo: " + str(newRadius))

#Pregunta 3 del questionario final del modulo 3
A = ['1', '2', '3']
for a in A:
    print(2*a)
