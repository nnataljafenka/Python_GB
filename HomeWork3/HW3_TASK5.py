def cum_sum():
    sum_cum = 0
    while True:
        sum_list = 0
        num = input("Введите числа, для выхода нажмите Q: ")
        num = num.replace('q', 'Q')
        num = num.split(' ')
        for i in num:
            try:
                sum_list += int(i)
            except ValueError:
                ""
        sum_cum += sum_list
        if num.count('Q'):
            return "The end"
        print(f"Промежуточная сумма: {sum_list}, Накопительная сумма: {sum_cum}")

print((cum_sum()))
