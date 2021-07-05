numbers = []
promedio, suma = 0, 0

try:
    for i in range(5):
        num = int(input(f'({i+1}) Digite un número '))
        numbers.append(num)
        suma += numbers[i]
        promedio = suma/len(numbers)

    print(f'El promedio total es {promedio}')
except ValueError:
    print('Error tiene que digitar un valor númerico')