class Room:
    def __init__(self):
        self.size = 12


class ClassRoom(Room):
    def __init__(self):
        super().__init__()
        self.students = ["Bill", "Mike"]


class Building:
    def __init__(self):
        self.room = Room()

    def SetRoomSize(self, NewRoomSize):
        self.room.size = NewRoomSize


SIN = Building()

print(SIN.room.size)

SIN.SetRoomSize(50)

print(SIN.room.size)

SIN406 = ClassRoom()

print(SIN406.size)
