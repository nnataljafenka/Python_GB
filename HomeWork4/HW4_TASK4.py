from random import randint
list_orig = [randint(1, 20) for el in range(randint(1, 51))]
my_list = [el for el in list_orig if list_orig.count(el) == 1]
print(list_orig)
print(my_list)