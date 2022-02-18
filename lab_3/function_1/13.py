import random

def guess(num, name, rnum, s):
    if num == rnum:
        print("Good job,", name + "! You guessed my number in", s, "guesses!")
    else:
        s += 1
        if num < rnum:
            print("Your guess is too low.\nTake a guess.")
            guess(int(input()), name, rnum, s)
        else:
            print("Your guess is too high.\nTake a guess.")
            guess(int(input()), name, rnum, s)

print("Hello! What is your name?")
n = input()
print("Well,", n + ", I am thinking of a number between 1 and 20.\nTake a guess.")
r = random.randint(1, 20)
s = 1
guess(int(input()), n, r, s)