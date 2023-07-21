#Diccionarios
#Son una especie de colecciones en Python, que muestran una lista de datos con un key (algo parecido a un objeto)
diccionario = { 
    "Thriller": "1982", 
    "Back in Black": "1980",
    "The Dark Side of the Moon": "1973",
    "The Bodyguard" : "1992",
    "Bat Out of Hell": "1977",
    "Their Greatest...": "1976",
    "Saturday Night Fever": "1977",
    "Rumours": "1977" 
}
print("Diccionario: " + str(diccionario))
#Para leer el valor del diccionario se tiene que ocupar la llave y este retornarà el valor asignado
print(diccionario["Thriller"]) #1982

#Tambien podemos agregar nuevas llaves con nuevos valors al diccionario
diccionario["Fragmentos"] = "2023"
print("Nuevo elemento 'Fragmentos': " + str(diccionario))

#Podemos eliminar elementos del diccionario con la función del() e indicando la llave del diccionario a eliminar
del(diccionario["Thriller"])
print("Se elimina la Key 'Thriller': " + str(diccionario))

#Podemos verificar si un elemento se encuentra en el diccionario utilizando el comando in
print("Se encuentra 'Rumours en el diccionario?: " + str('Rumours' in diccionario))
print("Se encuentra 'New Divine' en el diccionario?: " + str('New Divine' in diccionario))

#Tambien podemos mostrar la lista de keys que contiene el diccionario
print('Keys: ' + str(diccionario.keys()))

#De la misma manera se pueden obtener los valores del diccionario
print('Values: ' + str(diccionario.values()))
