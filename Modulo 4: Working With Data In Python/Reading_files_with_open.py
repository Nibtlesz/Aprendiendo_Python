"""
Descargar archivos
"""
#import urllib.request

#url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
#filename = "Ejemplo1.txt"
#urllib.request.urlretrieve(url,filename)

class File(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def openFile(self):
        file = ''
        with open(self.name,self.mode) as file:
            print(file.read())
        file.close()
        print(file.closed)
        
file = File('Ejemplo1.txt', 'r')
file.openFile()
