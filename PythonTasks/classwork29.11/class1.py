class Student():
    def __init__(self, name, point):
        self.name = name
        self.point = point
        self.course = None

    def output(self):
        print(self.name, self.point, self.course)

    def set_course(self, new_course):
        self.course = new_course

Kolya = Student('Kolya', 100)
Kolya.set_course('Programmer')
Kolya.output()
