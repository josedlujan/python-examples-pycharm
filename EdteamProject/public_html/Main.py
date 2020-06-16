from xml.etree.ElementTree import parse
import json
import csv
def crear_archivo():
    archivo = open('datos.txt','w')
    archivo.close()

def escribir_archivo():
    archivo = open('datos.txt','a')
    archivo.write('Jose Lujan\n')
    archivo.write('32334324324\n')
    archivo.write('Cancun')

def leer_archivo():
    archivo = open('datos.txt','r')
    linea = archivo.readline()
    while linea!= "":
        print(linea)
        linea = archivo.readline()
    archivo.close()

#crear_archivo()
#escribir_archivo()
#leer_archivo()

#xml
doc = parse('archivo.xml')
for elemento in doc.findall('nombre'):
    print(elemento.text)

#json
'''with open('archivo.json') as file:
    dato = json.load(file)
print(dato)
print(dato['nombres'][0]['apellido'])'''

'''doc_csv = open("archivo.csv","w")
csv_data = csv.writer(doc_csv)
lista = [["Jose",9982838474],["Juan",83838383],["pedro",172727272]]
#csv_data.writerow(lista)
for elemento in lista:
    csv_data.writerow(elemento)
doc_csv.close()

doc = open('archivo.csv',"r")
documento = csv.reader(doc)
for(nombre,numero) in documento:
    print(nombre,numero)
doc.close()'''

