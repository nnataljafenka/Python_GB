class Road:
    __meter_weight = 25
    __thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        result = round((self._length * self._width * self.__thickness * self.__meter_weight) / 1000, 2)
        return print(f"{self._length} м * {self._width} м * {self.__meter_weight} кг * {self.__thickness} см = {result} т")

road_1 = Road(20, 5000)
road_1.asphalt_mass()
