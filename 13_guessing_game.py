# Guessing Number Game

secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("Please input your number: "))
        if guess > secret_num:
            print("A bit smaller")
        elif guess < secret_num:
            print("A bit bigger")
    else:
        out_of_limit = True

if out_of_limit:
    print("Sorry, you lost!")
else:
    print("Congratulations, you won!")
