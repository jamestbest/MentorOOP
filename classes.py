class Animal:
    def __init__(self, age):
        self.age = age

    def SetAge(self, newAge):
        if (newAge < 0):
            print("can't be negative age")
        self.age = newAge

    def getAge(self):
        return self.age


cat = Animal(12)

print(cat.age)

cat.SetAge(-1)
cat.SetAge(10)

print(cat.age)