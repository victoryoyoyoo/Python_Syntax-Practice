# For Loop

# Syntax:
# for variable in string_OR_list:
#     code_to_execute_repeatedly

# for letter in "hello":
#     print(letter)

# for num in [0, 1, 2, 3, 4]:
#     print(num)

# for num in range(5):
#     print(num)

# for num in range(5, 10):
#     print(num)

print(pow(2, 6))
# Equivalent to: 2 * 2 * 2 * 2 * 2 * 2

# Implementing a custom power function using a for loop
def power(base, exp):
    result = base
    for index in range(exp - 1):
        result *= base
    return result

print(power(2, 6))