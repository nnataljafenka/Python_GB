from sys import argv


def salary():
    try:
        name, hh, wage_rate, prem = argv
        print((float(hh) * float(wage_rate)) + float(prem))
    except ValueError:
        print("Некорректный ввод! Введите выработку в часах, ставку в час и премию!")


salary()
