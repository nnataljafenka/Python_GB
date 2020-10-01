class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала!")

    def stop(self):
        print(f"Машина {self.name} остановилась!")

    def turn(self, direction):
        # w - прямо, s - назад, d - в право, a - в лево
        dir = {'w': 'прямо', 's': 'назад', 'd': 'в право', 'a': 'на лево'}
        print(f"Направление движения {self.name}: {dir.get(direction)}")

    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed} км\ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed} км\ч") if self.speed <= 60 else print(
            f"Скорость {self.name} превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name}: {self.speed} км\ч") if self.speed <= 40 else print(
            f"Скорость {self.name} превышена!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car_01 = TownCar(70, "red", "Mazda")
car_01.show_speed()
car_01.turn('w')
car_02 = PoliceCar(50, "white", "Audi")
car_02.go()
car_03 = WorkCar(30, "black", "КамАЗ")
car_03.turn('d')
car_03.stop()
car_04 = SportCar(100, "yellow", "Porsche")
print(car_04.color)
car_04.show_speed()