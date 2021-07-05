value = 32500
money = 50000
dev = money-value

print(f'El valor de la compra es de ${value} pesos')
print(f'El usuario paga con ${money} pesos\n')

if dev < 0:
    print(f'Hacen falta ${abs(dev)} pesos para pagar su compra')
else:
    print(f'El valor devuelta es de ${dev} pesos')
