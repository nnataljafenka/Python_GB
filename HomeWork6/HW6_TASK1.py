from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        while True:
            print("красный")
            sleep(7)
            print("желтый")
            sleep(2)
            print("зеленый")
            sleep(7)
            print("желтый")
            sleep(2)

tlight = TrafficLight()
tlight.running()