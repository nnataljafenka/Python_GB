from random import randint

list_orig = [randint(1, 999) for el in range(randint(1, 101))]
my_list = [list_orig[i] for i in range(1, len(list_orig)) if list_orig[i] > list_orig[i - 1]]
print(list_orig)
print(my_list)
