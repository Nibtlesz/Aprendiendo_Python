#Condiciones
#Las condiciones son sentencias que compara el valor de una variable con otro y retornan un valor booleando, dependiendo del valor retornado se cumplira una condición
#Para comparar datos necesitamos utilizar operadores logicos
a = 1

if ( a == 1):
    print("a es igual 1")

#En este ejemplo podemos observar que para indicar si la variable es igual a 1 se ocupa un doble igual, ya que si se deja con un solo igual este inicializará la variable con el dato
#Mayor que y mayor igual que
a = 5

if ( a > 1 ):
    print("a es mayor a 1")

if ( a >= 5):
    print("a es mayor o igual a 5")

#Menor que y Menor igual que
b = 4

if ( b < 6):
    print("b es menor que 6")

if ( b <= 4 ):
    print("b es menor igual que 4")

#Tambien podemos ocupar la sentencia else para que se ejecute otra acción en caso de que la condición principal no se cumpla

c = 10

if( c == 5 ):
    print("c es igual a 5")
else:
    print("c no es igual 5")

#Se pueden ocupar condiciones anidadas para que se ejecuten ciertas acciones dependiendo la condiciòn
age = 19

if ( age > 18):
    print("puedes entrar al concierto de AC/DC")
elif( age == 18):
    print("Puedes entrar al concierto de Pink Floyd")
else: 
    print("sigue tu camino")

#Operadores Logicos
#Los operadores logicos toman un dato booleano y retornan un dato booleano diferente
#Operador not()
#Este operador toma un dato booleano y retorna uno distinto true ----> return false
operator = True

if(not(operator) == False):
    print("el valor retornado es false")

#Operador OR
#Este operador devuelve un valor booleano True siempre y cuando se cumpla una de las dos condiciones
albumYear = 1990

if (albumYear < 1980) or ( albumYear > 1989):
    print("El album fue hecho en los 70's o 90's")
else:
    print("El album fue hecho en los 80's")

#Operador AND
#Este operador devuelve un valor boolleano TRUE, siempre y cuando las dos condiciones se cumplan
albumYear = 1980

if (albumYear < 1990) and ( albumYear > 1979):
    print("El album fue hecho en los 80's")