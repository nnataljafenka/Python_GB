# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

number = abs(int(input("Введите число: ")))
max_numb = 0
max_result = 0

while number:
    if (number % 10) != 0:
        max_numb = (number % 10)

    if max_numb > max_result:
        max_result = max_numb
    number //= 10

print(max_result)
