# Functions

def hello(name, age):
    # Code inside the function must be indented (usually 4 spaces)
    print("Hello, " + name + ". You are " + age + " years old.") 

# Call the function
# Note: If '20' is passed as an integer (20 instead of "20"), it will raise a TypeError. 
# Integers cannot be directly concatenated with strings without casting using str().
hello("yo", "20") 


def add(x, y):
    print(x + y)

# Call the function
add(5, 10) 

# Note: If there is no 'return' statement explicitly defined, the function will return 'None' by default.