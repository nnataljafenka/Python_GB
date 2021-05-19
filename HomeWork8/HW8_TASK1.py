class Data:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"год: {self.year}, месяц: {self.month}, день: {self.day}"

    @classmethod
    def set_date(cls, date):
        try:
            year, month, day = int(date[:4]), int(date[5:7]), int(date[8:])
            return cls(year, month, day)
        except ValueError:
            print("Некорректный ввод! Данные должны быть в формате YYYY*MM*DD, где * - любой элемент")

    @staticmethod
    def check_date(self):
        print(self.year) if self.year > 0 and self.year <= 9999 else print(
            "Некорректный год, значение должно быть от 1 до 9999")
        print(self.month) if self.month > 0 and self.month <= 12 else print(
            "Некорректный месяц, значение должно быть от 1 до 12")
        print(self.day) if self.day > 0 and self.day <= 31 else print(
            "Некорректный день, значение должно быть от 1 до 31")


date_01 = "2020-50-07"
date_02 = "2020-5o-070"
d1 = Data.set_date(date_01)
print(d1)
print()
Data.check_date(d1)

