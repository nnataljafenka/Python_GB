with open("hw5_file_01.txt", "w+", encoding='utf-8') as hw_file:
    while True:
        text = (input("Введите текст для записи: "))
        hw_file.write(f"{text}\n")
        if not text:
            break
