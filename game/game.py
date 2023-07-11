import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except ValueError:
        continue

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        break
    except ValueError:
        continue

if guess == number:
    print("Just right!")
elif guess < number:
    print("Too small!")
else:
    print("Too large!")