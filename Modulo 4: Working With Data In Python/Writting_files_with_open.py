class File(object):
    def __init__(self, name, mode, list):
        self.name = name
        self.mode = mode
        self.list = list

    def createFile(self):
        with open(self.name,self.mode) as writefile:
            writefile.write("This is line A")
            print("Archivo creado")

    def openFile(self):
        file = ''
        with open(self.name, self.mode) as readFile:
            file = readFile.read()
            return file
    
    def overwriteFile(self):
        with open(self.name, self.mode) as overwriteFile:
            for fileList in self.list:
                overwriteFile.write(fileList)
            print('Archivo reescrito')

#Creamos objeto
fileContent = File('Archivos/Example3.txt', 'w', []) 

#Crearemos un menú para que el usuario elija que quiere hacer con el archivo
opcion = ''
while(opcion != 'Q'):
    print("Menú")
    print("1.Crear archivo.\n2.Sobreescribir Archivo.\n3.Agregar lineas de texto al archivo.\n4.Abrir Archivo.\nQ.Salir")
    opcion = str(input("Que opción elijes?: "))

    if (opcion == '1'):
        fileContent.createFile()
        print("Regresando al menú...")
    elif (opcion == '2'):
        fileContent.list = ['This is Line AA\n', 'This is Line AB\n', 'This is Line AC\n']
        print(fileContent.list)
        fileContent.overwriteFile()
        print("Regresando al menú...")
    elif (opcion == '3'):
        print("Regresando al menú...")
    elif (opcion == '4'):
        fileContent.mode = 'r'
        file = fileContent.openFile()
        print(file)
        print("Regresando al menú...")
    else:
        opcion = 'Q'
        print("Fin del proceso")



