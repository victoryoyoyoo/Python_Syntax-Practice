from person import Person
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def print_school(self):
        print(self.school)
