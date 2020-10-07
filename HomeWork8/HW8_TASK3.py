class ListNumError(Exception):

    def __init__(self, text):
        self.text = text


list_num = []
while True:
    el = input("Введите число, для выхода введите Q: ")
    if el == "Q":
        break

    try:
        res = int(el)
        list_num.append(el)
    except ValueError:
        print(f"{el} - не является числом")

print(list_num)