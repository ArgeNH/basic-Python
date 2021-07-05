numbers = []

try:
    number = int(input('Digite la cantidad de datos que quiere ingresar: '))
    
    for i in range(number):
        num = int(input('Digite un numero: '))
        numbers.append(num)
except ValueError:
    print('Solo valores numericos enteros')
    exit()

print(f'Matriz normal {numbers}')
numbers.reverse()
print(f'Matriz invertida {numbers}')