my_list = list(input())
res_list = list()
print(f'исходный список = {my_list}')
# res_list1 = my_list[0::2]
# res_list2 = my_list[1::2]

for i in range(0, len(my_list), 2):
    if i + 1 < len(my_list):
        res_list.append(my_list[i + 1])
        res_list.append(my_list[i])
    else:
        res_list.append(my_list[i])
        break
print(res_list)
