class Motor:
    def __init__(self):
        self.speed = 0


class ElectricMotor(Motor):
    def __init__(self):
        super().__init__()
        self.battery = 100


class GasMotor(Motor):
    def __init__(self):
        super().__init__()
        self.fuel = 100


class CarWithInheritance(Motor):
    def __init__(self):
        super().__init__()


class CarWithComposition:
    def __init__(self, motor):
        self.motor = motor


if __name__ == "__main__":
    car = CarWithInheritance()
    print(car.speed)

    # the inheritance version of the car cannot have a different motor type i.e. electric or gas as it extends the Motor class
    # you would have to create a new class for each motor type e.g. ElectricCarWithInheritance, GasCarWithInheritance that extend their respective motor class

    car = CarWithComposition(ElectricMotor())
    print(car.motor.speed)
    print(car.motor.battery)

    car = CarWithComposition(GasMotor())
    print(car.motor.speed)
    print(car.motor.fuel)

    # the composition version of the car can have a different motor type i.e. electric or gas as it takes a motor object as a parameter
    # this can be extended to other attributes e.g. wheels, seats, etc.

    # please note that although when I showed the code examples of composition and aggregation I said that if it is initialized in the constructor then it is composition
    # it can also be composition if it is initialized in the class call e.g. car = CarWithComposition(ElectricMotor())
    # as the ElectricMotor() object can only be accessed via the CarWithComposition object

    # the difference in code between composition and aggregation is that you can access the aggregated object directly
    # but with composition you can only access the object via the class that it is composed in

    # e.g. motor = Motor()
    #      car = CarWithAggregation(motor)
    #      print(car.motor.speed)
    #      print(motor.speed)
    #      the motor object can be accessed directly so even when the car is destroyed the motor object will still exist

    #      car = CarWithComposition(Motor())
    #      print(car.motor.speed)
    #      print(motor.speed) # this will throw an error as the motor object can only be accessed via the CarWithComposition object


# inheritance version of gas and electric car
class ElectricCarWithInheritance(ElectricMotor):
    def __init__(self):
        super().__init__()


class GasCarWithInheritance(GasMotor):
    def __init__(self):
        super().__init__()
