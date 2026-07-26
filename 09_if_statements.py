# If Statements and Conditions

# 1.
# If I am hungry
#      I will go eat
hungry = True
if hungry:
    print("I will go eat")

# 2.
# If it rains today
#      I will drive to work
# Else 
#      I will walk to work
rainy = True
if rainy:
    print("I will drive to work")
else:
    print("I will walk to work")

# 3.
# If you score 100
#      I will give you $1000
# Else if you score 80 or above
#      I will give you $500
# Else if you score 60 or above
#      I will give you $100
# Else
#      You give me $300
score = 100
if score == 100:
    print("I will give you $1000")
elif score >= 80:
    print("I will give you $500")
elif score >= 60:
    print("I will give you $100")
else:
    print("You give me $300")

# 4.
# If you score 100 AND it rains today
#      I will give you $1000
# Else
#      You give me $100
score = 100
rainy = True
if score == 100 and rainy:
    print("I will give you $1000")
else:
    print("You give me $100")

# 5.
# If you score 100 OR it rains today
#      I will give you $1000
# Else
#      You give me $100
score = 100
rainy = True
if score == 100 or rainy:
    print("I will give you $1000")
else:
    print("You give me $100")

# 6.
# If you score 100 OR it does NOT rain today
#      I will give you $1000
# Else
#      You give me $100
score = 100
rainy = True
if score == 100 or not(rainy):
    print("I will give you $1000")
else:
    print("You give me $100")

# 7.
# If you do NOT score 100 OR it does NOT rain today
#      I will give you $1000
# Else
#      You give me $100
score = 100
rainy = True
if score != 100 or not(rainy):
    print("I will give you $1000")
else:
    print("You give me $100")

# Function to find the maximum among three numbers
def max_num(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(max_num(2, 3, 5))