# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите секунды: "))
in_minutes = 60
in_hours = 3600
result_hours = seconds // in_hours
result_minutes = (seconds % in_hours) // in_minutes
print(f"{result_hours:02.0f}:{result_minutes:02.0f}:{seconds % in_minutes:02.0f}")
