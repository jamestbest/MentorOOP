class Motor:
    def __init__(self):
        self.speed = 0


class Door:
    def __init__(self):
        self.open = False


class Car:
    def __init__(self):
        self.motor = Motor()
        self.driverDoor = Door()


def printCarInfo():
    car = Car()
    print(car.motor.speed)
    print(car.driverDoor.open)


if __name__ == "__main__":
    printCarInfo()