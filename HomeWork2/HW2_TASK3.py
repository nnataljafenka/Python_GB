user_month = int(input("Введите месяц в формате от 1 до 12: "))
period = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
flag = False
# flag - для выхода из цикла, если уже нашли нужный период
if user_month in range(0,12):
    for key in period:
        for el in period.get(key):
            if el == user_month:
                print(f'Время года - {key}')
                flag = True
                break
        if flag:
            break
else:
    print("Данные введены некорректно!")