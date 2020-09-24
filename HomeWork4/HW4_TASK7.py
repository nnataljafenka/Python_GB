def fact(n):
    if n < 0:
        yield "Введено отрицательное число!"
    else:
        res = 1
        for el in range(1, n + 1):
            res *= el
        yield f"{n}! = {res}"


for el in fact(int(input("Введите число:"))):
    print(el)
