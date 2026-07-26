# How to use strings and string operations

# Newline character \n
print("Hello\nyo")

# How to print quotation marks inside a string (Escape character)
print("Hello \" yo")

# String concatenation
print("Hello" + " " + "yo")      


# String methods (functions)
phrase = "aBcDeF"
print(phrase.lower()) # Convert all characters to lowercase
print(phrase.upper()) # Convert all characters to uppercase
print(phrase.islower()) # Check if the string is entirely lowercase, returns True or False
print(phrase.isupper()) # Check if the string is entirely uppercase, returns True or False
print(phrase.lower().islower()) # Methods can be chained; this will always return True
print(phrase[0]) # Access character by index (strings are 0-indexed)
print(phrase.index("B")) # Find the index of "B" (returns the index of the first occurrence if there are multiple)
print(phrase.replace("B", "X")) # Replace "B" with "X" (replaces all occurrences of "B" with "X")