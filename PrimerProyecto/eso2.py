def mi_primera_funcion():
    print('funcion')

def cuadrado(n):
    print (n*n)

def retorno_cuadrado(n):
    return  n*n


mi_primera_funcion()
cuadrado(8)
retorno_cuadrado(8)
#print(cuadrado(8))
print(retorno_cuadrado(8))
dato = retorno_cuadrado(10)
print(dato)

n = int(input("Ingresa el número"))
print("El cuadrado del número es:",retorno_cuadrado(n))