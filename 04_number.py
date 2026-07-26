# How to use numbers and numeric operations

print(-3.14)
print(8 / 5)
print(8 // 5)
print(8 + 8 * 5)
print((8 + 8) * 5)
print(8 % 5)

# Built-in functions
print(str(8)) # Convert to string ("8")
print(int("8")) # Convert string to integer (8)
print(abs(-8)) # Absolute value (8)
print(pow(2, 4)) # 2 to the power of 4 (2^4)
print(max(2, 3, 4, 5, 6)) # Return the maximum value
print(min(2, 3, 4, 5, 6)) # Return the minimum value
print(round(3.14159, 2)) # Round to 2 decimal places (defaults to nearest integer if the second argument is omitted)


from math import *

print(floor(3.14159)) # Round down (floor)
print(ceil(3.14159)) # Round up (ceiling)
print(sqrt(16)) # Square root