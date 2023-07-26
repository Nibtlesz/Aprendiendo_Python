"""
Descargar archivos
"""
#import urllib.request

#url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
#filename = "Ejemplo1.txt"
#urllib.request.urlretrieve(url,filename)

#Clase archivo
class File(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def openFile(self, numero):
        file = ''
        if (numero):
            with open(self.name,self.mode) as file:
                return (file.read(numero))
        else:
            with open(self.name,self.mode) as file:
                return (file.read())
    def openFile2(self):
        file = ''
        with open(self.name, self.mode) as file:
            print(file.read(4))
            print(file.read(4))
            print(file.read(7))
            print(file.read(15))

#Ejecuciòn de la clase
file = File('Ejemplo1.txt', 'r')
fileContent = file.openFile("")
print(fileContent)
file.openFile2()
