user_str = input("Введите строку: ")
print(user_str.split(' '))

for ind, el in enumerate(user_str.split(' '), 1):
    print(f'Строка под № {ind}: {el[0:10]}')