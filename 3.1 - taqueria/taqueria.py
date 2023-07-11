import sys

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

sum = 0.0

while True:
    try:
        item = input("Item: ").strip().title()
        sum += menu[item]
    except (KeyError, ValueError):
        continue
    except EOFError:
        print("\n")
        break
    else:
        print(f"${sum:.2f}")