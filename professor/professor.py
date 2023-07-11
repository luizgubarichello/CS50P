import random


def main():
    level = get_level()
    numbers = []
    score = 0
    for i in range(20):
        numbers.append(generate_integer(level))
        attempts = 0
        while i % 2 == 1:
            try:
                answer = int(input(f"{numbers[i]} + {numbers[i-1]} = "))
            except ValueError:
                print("EEE")
                attempts+=1
            else:
                if answer != (numbers[i] + numbers[i-1]):
                    print("EEE")
                    attempts+=1
                else:
                    score+=1
                    break
            if attempts == 3:
                print(f"{numbers[i]} + {numbers[i-1]} = {numbers[i] + numbers[i-1]}")
                break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError()


if __name__ == "__main__":
    main()