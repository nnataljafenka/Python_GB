class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя сотрудника: {self.name} \nФамилия сотрудника: {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии: {sum(self._income.values())}")

worker_1 = Position("Kate", "Petrova", "Director", 100, 20)
worker_1.get_full_name()
worker_1.get_total_income()


