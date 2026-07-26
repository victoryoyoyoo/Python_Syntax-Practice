# Inheritance Example
from student import Student

# Create a Student object
student1 = Student("yo", 87, "yo Elementary School")

# Call methods (some are defined in Student, some are inherited from Person)
student1.print_school()
student1.print_age()
student1.print_name()