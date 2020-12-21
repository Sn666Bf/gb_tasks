# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


time_sec = int(input('Введите время в секундах: '))
time_min = 0
time_hours = 0


if time_sec < 60:
    result = str(f'{time_hours} : {time_min} : {time_sec}')
    print(result)

elif (time_sec >= 60) and (time_sec < 3600):
    time_min = time_sec // 60
    time_sec = time_sec - (time_min * 60)
    result = str(f'{time_hours} : {time_min} : {time_sec}')
    print(result)

elif time_sec >= 3600:
    time_hours = time_sec // 3600
    time_min = (time_sec % 3600) // 60
    time_sec = time_sec - (time_hours * 3600 + time_min * 60)
    result = str(f'{time_hours} : {time_min} : {time_sec}')
    print(result)

