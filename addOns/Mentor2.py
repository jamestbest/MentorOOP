# class - Train
# has passengers
# has cars
# two functions - move and derail

class Cars:
    def __init__ (self, Passengers):
        self.passengers = Passengers

    def detach(self):
        print("i have detached")


class FirstClassCars (Cars):
    def __init__ (self, passengers):
        super().__init__(passengers)

        self.serviceTrolley = "Trolley"

    def detach (self):
        print("no")


class Train:
    def __init__ (self, passengers, firstClassPassengers):
        self.cars = Cars(passengers)
        self.firstClass = FirstClassCars(firstClassPassengers)

        self.position = [0,0]

    def move(self, direction):
        self.position[0] = self.position[0] + direction[0]
        self.position[1] = self.position[1] + direction[1]


passengers = ["a","b","c"]
firstClassPassengers = ["d","e"]
thomas = Train(passengers, firstClassPassengers)

print(thomas.firstClass.passengers)
print(thomas.cars.passengers)
print(thomas.position)

thomas.move([1,2])

print(thomas.position)

thomas.cars.detach()

thomas.firstClass.detach()

allCars = [thomas.firstClass, thomas.cars]
print("-----------")
for car in allCars:
    car.detach()