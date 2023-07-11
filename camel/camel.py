word = input("camelCase: ")

for letter in word:
    if letter.isupper():
        word = word.replace(letter,f"_{letter.lower()}")

print(f"snake_case: {word}")