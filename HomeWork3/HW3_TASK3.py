def my_func(arg1=0, arg2=0, arg3=0):
    """ Функция возвращает сумму наибольших двух аргументов """
    my_list = (arg1, arg2, arg3)
    try:
        return sum(my_list) - min(my_list)
    except TypeError:
        return "Все аргументы должны быть числами!"


print(my_func(30, 5, 20))
