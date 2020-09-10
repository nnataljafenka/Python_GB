
proc = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if proc > costs:
    print("Финансовый результат - прибыль")
    profit = (proc - costs)
    profitability = round(profit / proc, 2) * 100
    print(f"Рентабельность: {profitability} %")
    employees = int(input("Введите кол-во сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника: {round(profit / employees, 2)}")
else:
    print("Финансовый результат - убыток :(")