import os
import math
""" n = 5
while n > 0:
    print(f'el valor de n: {n}')
    n = n-1

print('\n')

m = 0
while m < 4:
    print(f'El valor de m: {m}')
    m = m + 1 """


""" age = 0
while age < 100:
    if (age < 18):
        print(f'{age} menor de edad')

    elif (age < 70):
        print(f'{age} adulto')

    else:
        print(f'{age} mayor de edad')
    age = age + 1

print('Fin del programa') """

os.system('cls')

""" while True:
    tex = input('Ingrese un texto: ')
    if tex == 'fin':
        break
    print(f'Acaba de escribir la cadena: {tex}')
print('Fin del programa')
"""

""" while True:
    num = int(input('Ingrese un numero: '))

    if num < 5:
        continue
    if num > 10:
        break

    print(f'Se escribio {num}')
print('Fin') """

""" R = 6372.795477598

list = [[6.691,-72.8727],[6.567,-73.120],[6.456,-72.872]]
data = [
    [6.632, -72.984, 285], 
    [6.564, -73.061, 127], 
    [6.531, -73.002, 15], 
    [6.623, -72.978, 56]]
    

lat_2 = list[0][0]
lon_2 = list[0][1]

distances = []
ct = 0
for i in data:
    aux = math.pow(math.sin((i[0] - lat_2)/2),2)
    aux_2 = math.pow(math.sin((i[1] - lon_2)/2),2)
    val_1 = math.cos(i[0])*math.cos(lat_2) 
    total = int(2*R*math.asin(math.sqrt(aux+(val_1*aux_2))))
    distances.append(total)


count = 0
for i in distances:
    data[count].append(i)
    count+=1
print(data)

x = sorted(data, key=lambda i: i[2])
print(x)
print(f'La zona wifi 1: ubicada en [\'{x[0][0]}\',\'{x[0][1]}\'] a {x[0][3]} metros, tiene en promedio {x[0][2]} usuarios')
print(f'La zona wifi 2: ubicada en [\'{x[1][0]}\',\'{x[1][1]}\'] a {x[1][3]} metros, tiene en promedio {x[1][2]} usuarios')
opt_2 = int(input('Elija 1 o 2 para recibir indicaciones de llegada\n')) """

"""
menor = 99999
pos = 0
pos_2 = 0
aux = 0
for i in data:
    #print(i[3])
    if menor > i[3]:
        menor = i[3]
        pos += 1
    else:
        pos_2 += 1
        aux = i[3]
    print(f'El menor es {menor} con posición {pos} y el {aux} y pos {pos_2}')
print(f'El menor es {menor} con posición {pos} y anterior {aux} y pos {pos_2}')

lower = 0
pos_3 = 0
for i in data:
    print(i[2])
    if i[2] >= i[2]:
        lower = i[2]

print(lower)
"""

#x = data[pos].index(menor)
# print(x)

#distance = 2 * R * math.asin(math.sqrt((math.sin(v_lat/2)**2)+math.cos(lat_1)*math.cos(lat_2)*math.sin(v_lon/2)**2))
# print(distance)

""" def show_list():
    enum = 0
    for i in list:
        enum += 1
        print(f'coordenada [latitud, longitud] {enum} : {i}')

show_list()

menor = 0
pos = 0
for i in list:
    if i[1] < menor:
        pos += 1
        menor = i[1]

print(menor,' ', pos) """

""" notas = []
sum = 0

try:
    for i in range(100):
       nt = float(input('Ingrese sus notas: '))
       notas.append(nt)
       sum += nt
except ValueError:
    print('Se ha ingresado fin\n')

notas.sort()
print(f'La nota mas baja fue: {notas[0]}')
notas.sort(reverse=True)
print(f'La nota mas alta fue: {notas[0]}')
promedio = round(sum/len(notas),1)
print(f'El promedio final es: {promedio}')
if promedio <= 3.0:
    print('Perdio la materia')
else:
    print('Felicidades, Gano la materia') """

import pandas as pd
import csv

data = [[6.632, -72.984, 285], [6.564, -73.061, 127], [6.531, -73.002, 15], [6.623, -72.978, 56]]

information = [{'actual': data[0], 'zonawifi1': data[1], 'recorrido' : data[2]+data[3]}]

pd.DataFrame(information).to_csv('information.csv', index=False)

s = pd.Series(information)
print(s)
