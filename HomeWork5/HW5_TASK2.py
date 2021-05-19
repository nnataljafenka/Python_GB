with open("hw5_file_02.txt", "r", encoding='utf-8') as hw_file:
    count_word = 0
    line_list = hw_file.readlines()
    print(f" Кол-во строк: {len(line_list)}")
    for i, el in enumerate(line_list, 1):
        count_word = len(el.split())
        print(f" Кол-во слов в {i} - й строке : {count_word}")

