class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)


class Teacher:
    def __init__(self, students):
        self.students = students

    def printStudents(self):
        for student in self.students:
            student.printInfo()


if __name__ == "__main__":
    students = [Student("John", 18), Student("Jane", 19)]
    teacher = Teacher(students)
    teacher.printStudents()

    print("---------Outside teacher----------")

    students[0].printInfo()