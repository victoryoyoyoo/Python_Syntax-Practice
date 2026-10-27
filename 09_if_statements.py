hungry = True
if hungry:
    print("I will go eat")

rainy = True
if rainy:
    print("I will drive to work")
else:
    print("I will walk to work")

score = 100
if score == 100:
    print("I will give you $1000")
elif score >= 80:
    print("I will give you $500")
elif score >= 60:
    print("I will give you $100")
else:
    print("You give me $300")

score = 100
rainy = True
if score == 100 and rainy:
    print("I will give you $1000")
else:
    print("You give me $100")

score = 100
rainy = True
if score == 100 or rainy:
    print("I will give you $1000")
else:
    print("You give me $100")

score = 100
rainy = True
if score == 100 or not(rainy):
    print("I will give you $1000")
else:
    print("You give me $100")

score = 100
rainy = True
if score != 100 or not(rainy):
    print("I will give you $1000")
else:
    print("You give me $100")

def max_num(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max_num(2, 3, 5))
