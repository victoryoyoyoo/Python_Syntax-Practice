file = open("123.txt", mode="r")
print(file.read())
file.close()

file = open("123.txt", mode="r")
for line in file:
    print(line)
file.close()

file = open("123.txt", mode="r")
print(file.readlines())
file.close()

with open("123.txt", mode="r") as file:
    print(file.read())
