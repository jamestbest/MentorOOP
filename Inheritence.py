class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def speak(self):
        print(f"I am an animal and my age is {self.age}")

    def setAge(self, newAge):
        if newAge < 0:
            print("cannot set age to be negative")
        else:
            self.age = newAge

    def getAge(self):
        return self.age

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

    cat = Cat("Pepper")

    cat.setAge(-1)
    cat.setAge(10)

    print(cat.getAge())

    print("--------Speaking--------")
    animals = [Dog("Clifford"), Cat("Garfield")]

    for animal in animals:
        animal.speak()

    print("---------Names----------")
    for animal in animals:
        print(animal.name)