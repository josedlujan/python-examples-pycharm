#tuplas
#almacenar datos no necesario del mismo tipo.
#inmutables
#ya definida no se pueden, agregar, borrar cambiar elementos.

tupla = (1,2,3)
tupla2 = ('a','b','c')
usuario = ('jose','20','Cancún')
print(tupla)
print(tupla2)
print(usuario)
#seleccionar un elemento de la tupla
print(tupla2[2])
#provocar un error
#tupla2[2] = 1
for elemento in usuario:
    print(elemento)


def enviar_datos():
    a=1
    b=2
    c=3
    return (a,b,c)

def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])

datos = enviar_datos()
recibir_datos(datos)
#recibir_datos(enviar_datos())


######Listas########
##Como las tuplas pero mutables

lista = [1,2,3]
lista2 = [1.1,1.2,1.3]
lista3 = ["a","b","c"]
lista4 = ["a",1,1.1]

print(lista4)

print(lista4[1])

for elemento in lista4:
    print(elemento)

#modificar una lista agregar
lista4.append(100)
print(lista4)
#modificar
lista4[3] = "f"
print(lista4)
#eliminar el indicado o el ultimo si no se indica alguno
lista4.pop()
print(lista4)
#agrega otra lista
lista4.extend([10,10,10])
print(lista4)

#agregar un elemento en una posicion especifica
lista4.insert(0,"aaaaaa")
print(lista4)

#borrar
del lista4[0]
print(lista4)

#remove
lista4.remove(10)
print(lista4)

#contar elmntos
print(lista4.count(10))

#ordenar
lista5 = [20,5,7,1,4,8]
lista5.sort()
print(lista5)

#invertido
lista5.sort(reverse=True)
print(lista5)

print(lista5[-1])
print(lista5[-2])


##DICCIONARIOS####
#elmento clave no se puede repetir
#
personas = {'libro 1':'Jose Lujan','libro 2':'Benito Juarez','Libro 3':'Obama'}
print(personas)
for persona in personas:
    print(persona)
print(personas['libro 2'])
print(personas.keys())
print(personas.values())

diccionario = {'a':(1,2),'b':(3,4),'c':(5,6)}
print(diccionario)
print(diccionario['b'])

#diccionarioX.clear deja vacio el diccionario

#copia el diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

print(diccionario2.get('a'))

#eliminar del diccionario pop
diccionario2.pop('a')
print(diccionario2)

#actualiza el diccionario recibiendo otro
diccionario3 = {'a':1,'b':(0,0)}
diccionario2.update(diccionario3)
print(diccionario2)

#funciones
import random
num = random.randint(1,10)
print(num)

from math import sqrt
n = sqrt(9)
print(n)