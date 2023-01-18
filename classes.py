class Animal:
    def __init__(self, age):
        self.__age = age # in Python, you can make a variable private by adding '__' in front of it's name
                         # protected variables are defined by adding '_' in front of it's name

    def SetAge(self, newAge):
        if newAge < 0:
            print("can't be negative age")
        self.__age = newAge

    def getAge(self):
        return self.__age


cat = Animal(12)

print(cat.getAge())

cat.SetAge(-1)
cat.SetAge(10)

print(cat.getAge())