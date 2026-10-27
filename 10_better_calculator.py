num1 = float(input("Please input your first number (num1): "))
op = input("Please input your operator (+, -, *, /): ")
num2 = float(input("Please input your second number (num2): "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Unsupported operation")
