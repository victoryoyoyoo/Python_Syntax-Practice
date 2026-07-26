# Classes and Objects

class Phone:
    # The __init__ method is the constructor used to initialize the object's attributes
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

    def add(self, number1, number2):
        return number1 + number2

# Create objects (instances) of the Phone class
phone1 = Phone("ios", 123, True)
print(phone1.number) # Accessing the 'number' attribute of phone1

phone2 = Phone("android", 456, False)
print(phone2.os) # Accessing the 'os' attribute of phone2

print(phone1.is_ios())

print(phone1.add(5, 6))