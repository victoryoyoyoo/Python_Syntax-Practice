# Original version (Without inheritance)

# class Student:
#     def __init__(self, name, age, school):
#         self.name = name
#         self.age = age
#         self.school = school
# 
#     def print_name(self):
#         print(self.name)
# 
#     def print_age(self):
#         print(self.age)
# 
#     def print_school(self):
#         print(self.school)
# 
# But since it has overlapping parts with Person, we can use inheritance!


# Which equals to the following:
from person import Person    # Must import the parent class for inheritance
class Student(Person):       # Don't forget the parentheses ()!
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)