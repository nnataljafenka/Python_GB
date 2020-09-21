def int_func(text):
    text_list = text.split()
    for word in text_list:
        flag = True
        # flag - флаг, исключающий печать некорректных слов
        for i in word:
            if ord(i) < 97 or ord(i) > 122:
                print(f" Некорректный ввод слова: {word}")
                flag = False
                break
        if flag: print(word.title())


int_func(input("Введите текст, каждое слово состоит из латинских букв в нижнем регистре: "))
# hjhj акпл fkап поgjj 123 Gfjjk
