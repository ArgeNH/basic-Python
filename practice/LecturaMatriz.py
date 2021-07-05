import numpy

fila = int(input('Ingrese el numero de fila: '))
columna = int(input('Ingrese el numero de columna: '))

matriz = []

for i in range(fila):
    matriz.append([])
    for j in range(columna):
        num = int(input('Ingrese un numero: '))
        matriz[i].append(num)

mat = numpy.array(matriz)
print(mat)