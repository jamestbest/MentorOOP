class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow")


if __name__ == "__main__":
    print("--------Speaking--------")
    animals = [Dog("Clifford"), Cat("Garfield")]
    for animal in animals:
        animal.speak()

    print("---------Names----------")
    for animal in animals:
        print(animal.name)

# • class
# • object
# • instantiation
# • encapsulation
# • inheritance
# • aggregation
# • composition
# • polymorphism
# • overriding
