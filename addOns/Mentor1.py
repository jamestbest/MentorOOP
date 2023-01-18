class Room:
    def __init__(self, roomSize):
        self.size = roomSize


class Classroom(Room):
    def __init__ (self, roomSize):
        super().__init__ (roomSize)
        self.students = ["asd","asdsd"]


class Building:
    def __init__(self):
        self.room = Room(12)

classroom1 = Classroom(13)

print(classroom1.size)
print(classroom1.students)