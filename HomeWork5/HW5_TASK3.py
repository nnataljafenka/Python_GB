with open("text_3.txt", "r", encoding='utf-8') as hw_file:
    line_list = hw_file.readlines()
    sum_salary = 0
    # print(line_list)
    print("Сотрудники с доходом менее 20 тыс. : ")
    for el in line_list:
        line = el.split()
        sum_salary += float(line[1])
        if float(line[1]) < 20000:
            print(line[0])
print(f"Средний доход: {sum_salary / len(line_list)}")