import os
import time
import math
import pandas as pd
import csv
#Reto 5

print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
name = '51699'
password = '99615'
list = []
data = [[6.632, -72.984, 285], [6.564, -73.061, 127], [6.531, -73.002, 15], [6.623, -72.978, 56]]
distances = []
opt_2 = 0

print('Ingrese su nombre de usuario:')
name_input = input()
if name_input == 'Tripulante2022':
    print('Este fue mi primer programa y vamos por más')
    time.sleep(1)
    exit()
elif name_input == name:
    print('Nombre de usuario valido')
else:
    print('Error')
    time.sleep(1)
    exit()

def lats_pss():
    suma = 0
    cont = 0
    num_lat = int(input('¿Cuántas latitudes vas a ingresar? '))
    for i in range(num_lat):
        lat_cod = float(input(f'Ingrese latitud {i+1} '))
        suma +=lat_cod
        cont +=1
    promedio = suma/cont
    print(f'El promedio es: {promedio}')
    time.sleep(1)
    exit()


print('Ingrese su contraseña: ')
password_input = input()
if password_input == 'm1s10nt1c':
    lats_pss()
elif password_input == password:
    print('Contraseña valida')
else:
    print('Error')
    time.sleep(1)
    exit()

code = '51699'
num_uno = int(str(code)[-3:])
num_dos = 5+9-6+1
print(f'Cuál es el valor de : {num_uno} + {num_dos} ?:')
captcha_input = int(input())
if captcha_input == num_uno + num_dos:
    print('Sesión iniciada')
else:
    print('Error')
    time.sleep(1)
    exit()

os.system('clear')
print("Sesión iniciada")

options = ['Cambiar contraseña',
           'Ingresar coordenadas actuales',
           'Ubicar zona wifi más cercana',
           'Guardar archivo con ubicación cercana',
           'Actualizar registros de zonas wifi desde archivo',
           'Elejir opción de menú favorita',
           'Cerrar sesión']


def menu():
    count = 0
    for i in options:
        count += 1
        print(f'{count}. {i}')


def ch_passwd():
    global password
    print('Cambio de contraseña')
    password_current = input('Digite su contraseña actual:\n')
    if password_current == password:
        psd = input('Ingrese nueva contraseña:\n')
        if psd != password:
            print('Contraseña modificada')
            password = psd
        else:
            print('Error')
            time.sleep(1)
            exit()
    else:
        print('Error')  # Contraseña de actual incorrecta
        time.sleep(1)
        exit()


def validate_coords_lat(coords):
    if coords != '':
        try:
            num = round(float(coords), 3)
        except ValueError:
            print('Error coordenada')
            exit()
        if num >= 6.532 and num <= 6.690:
            print('ok')
        else:
            print('Error coordenada')
            time.sleep(1)
            exit()
    else:
        print('Error')
        time.sleep(1)
        exit()
    return num


def validate_coords_long(coords):
    if coords != '':
        try:
            num = round(float(coords), 3)
        except ValueError:
            print('Error coordenada')
            exit()
        if num >= -73.120 and num <= -72.872:
            print('ok')
        else:
            print('Error coordena')
            time.sleep(1)
            exit()
    else:
        print('Error')
        time.sleep(1)
        exit()
    return num


def coord():
    global list
    list.append([])
    list.append([])
    list.append([])
    print('Ingresar coordenadas: ')
    time.sleep(0.5)

    work_lat = input('Latitud trabajo: ')
    work_lat_c = validate_coords_lat(work_lat)
    work_long = input('Longitug trabajo: ')
    work_long_c = validate_coords_long(work_long)
    list[0].append(work_lat_c)
    list[0].append(work_long_c)

    home_lat = input('Latitud casa: ')
    home_lat_c = validate_coords_lat(home_lat)
    home_long = input('Longitug casa: ')
    home_long_c = validate_coords_long(home_long)
    list[1].append(home_lat_c)
    list[1].append(home_long_c)

    park_lat = input('Latitud parque: ')
    park_lat_c = validate_coords_lat(park_lat)
    park_long = input('Longitud parque: ')
    park_long_c = validate_coords_long(park_long)
    list[2].append(park_lat_c)
    list[2].append(park_long_c)
    print('Se añadieron las coordenadas')


def update_coords(opt):
    print('Vamos a actualizar')
    global list
    if opt == 1:
        # Eliminar coordenada en la lista
        list[0].pop()
        list[0].pop()
        # Actualizar coordenada
        work_lat = input('Latitud trabajo: ')
        work_lat_c = validate_coords_lat(work_lat)
        work_long = input('Longitug trabajo: ')
        work_long_c = validate_coords_long(work_long)
        list[0].append(work_lat_c)
        list[0].append(work_long_c)
    elif opt == 2:
        list[1].pop()
        list[1].pop()
        # Actualizar coordenadas
        home_lat = input('Latitud casa: ')
        home_lat_c = validate_coords_lat(home_lat)
        home_long = input('Longitug casa: ')
        home_long_c = validate_coords_long(home_long)
        list[1].append(home_lat_c)
        list[1].append(home_long_c)
    elif opt == 3:
        list[2].pop()
        list[2].pop()
        # actualizar coordenadas
        park_lat = input('Latitud parque: ')
        park_lat_c = validate_coords_lat(park_lat)
        park_long = input('Longitud parque: ')
        park_long_c = validate_coords_long(park_long)
        list[2].append(park_lat_c)
        list[2].append(park_long_c)
    elif opt == 0:
        print('Regreso menú')
    else:
        print('Error actualización')
        time.sleep(1)
        exit()


def show_list():
    enum = 0
    for i in list:
        enum += 1
        print(f'coordenada [latitud, longitud] {enum} : {i}')

def calc_time(mts):
    time_auto = round(mts/20.83,3)
    print(f'Tiempo en auto = {time_auto} min')
    time_bici = round(mts/3.33,3)
    print(f'Tiempo en bici = {time_bici} min')


def calc(lat, long):
    global distances
    R = 6372.795477598
    global data
    print('Zonas wifi cercanas con menos usuarios')
    for i in data:
        aux = math.pow(math.sin((i[0] - lat)/2),2)
        aux_2 = math.pow(math.sin((i[1] - long)/2),2)
        val_1 = math.cos(i[0])*math.cos(lat) 
        total = int(2*R*math.asin(math.sqrt(aux+(val_1*aux_2))))
        distances.append(total)

    count = 0
    for i in distances:
        data[count].append(i)
        count += 1

    x = sorted(data, key=lambda i: i[2])
    print(f'La zona wifi 1: ubicada en [\'{x[0][0]}\',\'{x[0][1]}\'] a {x[0][3]} metros, tiene en promedio {x[0][2]} usuarios')
    print(f'La zona wifi 2: ubicada en [\'{x[1][0]}\',\'{x[1][1]}\'] a {x[1][3]} metros, tiene en promedio {x[1][2]} usuarios')
    opt_2 = int(input('Elija 1 o 2 para recibir indicaciones de llegada\n'))
    if opt_2 == 1:
        dc = x[0][3]
        print('Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur')
        calc_time(dc)
    elif opt_2 == 2:
        dc = x[1][3]
        print('Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte')
        calc_time(dc)
    else:
        print('Error zona wifi')
        time.sleep(1)
        exit()
    retrieve = int(input('Presione 0 para salir\n'))
    if retrieve == 0:
        print('Regresando menu principal')
    else:
        print('Error')
        time.sleep(1)
        exit()

actual = 0
def calc_distance(opt):
    global actual
    actual = opt
    print(actual, ' <-- actual')
    if opt == 1:
        print('Coordenada 1')
        lat_1 = list[0][0]
        long_1 = list[0][1]
        calc(lat_1, long_1)
    elif opt == 2:
        print('Coordenada 2')
        lat_2 = list[1][0]
        long_2 = list[1][1]
        calc(lat_2, long_2)
    elif opt == 3:
        print('Coordenada 3')
        lat_3 = list[2][0]
        long_3 = list[2][1]
        calc(lat_3, long_3)
    else:
        print('Error ubicación')
        time.sleep(1)
        exit()


def export_file(exp, dict_info):
    if exp == 1:
        print('Exportando archivo')
        #cv_list= list(dict_info)
        #pd.DataFrame(cv_list).to_csv('dates.csv', index=False)
        time.sleep(1)
        exit()
    else:
        print('Volviendo menu principal')


def update_data():
    print('Actualizando coords')


def action(num):
    count = 0
    if num == 1:
        print(f'Usted ha elegido la opción {num}')
        ch_passwd()
    elif num == 2:
        print(f'Usted ha elegido la opción {num}')
        if not list:
            coord()
        else:
            print('Actualizar coordenadas')
            show_list()

            menor = 0
            pos = 0
            for i in list:
                if i[1] < menor:
                    pos += 1
                    menor = i[1]
            print(f'La coordenada {pos} es la que esta más al occidente')

            pr_long = round((list[0][1]+list[1][1]+list[2][1])/3, 3)
            pr_lat = round((list[0][0]+list[1][0]+list[2][0])/3, 3)
            print(f'El promedio de todos los puntos es [{pr_lat},{pr_long}]')
            opt = int(input(
                'Presione 1, 2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú:\n'))
            update_coords(opt)
    elif num == 3:
        print(f'Usted ha elegido la opción {num}')
        if not list:
            print('Error sin registro de coordenadas')
            time.sleep(1)
            exit()
        else:
            print('Ubicar zona wifi más cercana')
            show_list()
            opt_2 = int(input('Por favor elija su ubicación actual (1, 2 ó 3) para calcular la distancia a los puntos de conexión\n'))
            calc_distance(opt_2)
    elif num == 4:
        global actual
        print(f'Usted ha elegido la opción {num}')
        if list == [] or distances == []:
            print('Error de alistamiento')
            time.sleep(1)
            exit()
        else:
            print('Guardar archivo con ubiación cercana')
            information = {'actual': list[actual-1], 'zonawifi1': data[0], 'recorrido' : distances[0]+distances[1]}
            print(f'informacion = {information}')
            exp_opt = int(input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal\n'))
            export_file(exp_opt, information)
    elif num == 5:
        print(f'Usted ha elegido la opción {num}')
        update_data()
        num_opt = int(input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal\n'))
        if num_opt == 0:
            print('Regresando al menu principal')
    elif num == 6:
        number = int(input('Seleccione opción favorita:\n'))
        if number > 0 and number <= 5:
            print("""Para confirmar por favor responda:
            Si me giras pierdo tres unidades por
            eso siempre debes colocarme de pie,
            la respuesta es:""")
            riddle_one = int(input())
            if riddle_one == num_dos:
                print('Correcto')
                print("""Para confirmar por favor responda:
                Pues de una manera soy un número par
                pero paso a ser otro si la vuelta me das,
                la respuesta es:""")
                riddle_two = int(input())
                if riddle_two == num_dos:
                    check = options.pop(number-1)
                    options.insert(0, check)
                    time.sleep(1)
                else:
                    count += 1
                    if count == 1:
                        print('Error')
            else:
                count += 1
                if count == 1:
                    print('Error')

            os.system("clear")
        else:
            print('Error')
            time.sleep(1)
            exit()
        time.sleep(2)
    elif num == 2021:
        print('Dame una latitud y te diré cual hemisferio es...')
        hem = float(input('Digite coordenada: '))
        if hem <= -1:
            print('Usted está en hemisferio sur')
            exit()
        else:
            print('Usted está en hemisferio norte')
            exit()
    elif num == 2022:
        cord_long = float(input('Escribe una la coordenada de una longitud en Sudamérica y te diré su huso horario\n'))
        if cord_long >= -81.296 and cord_long <= -67.401:
            print('El huso horario es -5')
        elif cord_long >= -67.402 and cord_long <= -54.316:
            print('El huso horario es -4')
        else:
            print('El huso horario es -3')
        exit()
    elif num == 7:
        print('Hasta pronto')
        exit()


count = 0
while True:
    menu()
    try:
        option = int(input('Elija una opción:\n'))
        if option > 0 and option < 8 or option == 2021 or option == 2022:
            action(option)
        else:
            count += 1
            print('Error')
            time.sleep(1)
    except ValueError:
        count += 1
        print('Error')
        time.sleep(1)
    if count == 4:
        print('Error')
        time.sleep(1)
        exit()