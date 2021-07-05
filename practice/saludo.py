from datetime import datetime

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
hour = int(current_time[:2])

if hour >= 6 and hour < 12:
    print(f'Buenos dias, la hora es {current_time[:5]}am ')
elif hour >= 12 and hour < 18:
    print(f'Buenas tardes, la hora es {current_time[:5]}pm')
else:
    if hour >= 0 and hour < 6:
        print(f'Es de madrugada, la hora es {current_time[:5]}am')
    else:
        print(f'Buenas noches, la hora es {current_time[:5]}pm')
    