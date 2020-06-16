archivo = "/Users/jose/Desktop/archivo.txt"
palabraBuscar = "Python"
repetidas = 0

file = open(archivo)
lines = file.readlines()

for line in lines:
    palabras = line.split(' ')
    for palabra in palabras:
        if(palabra==palabraBuscar):
            repetidas = repetidas + 1

print('La palabra {} tiene {} repeticiones en el archivo {}'.format(palabraBuscar,repetidas,archivo))