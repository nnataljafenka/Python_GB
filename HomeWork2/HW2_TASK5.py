my_list = [7, 5, 3, 3, 2]
res_list = my_list
user_num = int(input("Введите число: "))

if my_list[-1] > user_num:
    res_list.append(user_num)
else:
    for el in my_list:
        if user_num >= el:
            res_list.insert(res_list.index(el), user_num)
            break
print(res_list)