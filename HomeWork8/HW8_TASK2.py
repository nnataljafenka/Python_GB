class ZeroError(Exception):

    def __init__(self, text):
        self.text = text


num = input("Введите числитель: ")
den = input("Введите знаменатель: ")

try:
    if float(den) == 0:
        raise ZeroError("Вы ввели отрицательное число!")
    res = round(float(num) / float(den), 4)
except (ValueError, ZeroError) as err:
    print(err)
else:
    print(f"Результат: {res}")
