class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандаша {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркера {self.title}")

draw_01 = Pen("Parker")
draw_01.draw()
draw_01 = Pencil("Crayola")
draw_01.draw()
draw_01 = Handle("MARKER")
draw_01.draw()