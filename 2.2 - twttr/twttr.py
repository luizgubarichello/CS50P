phrase = input("Input: ").strip()

for letter in phrase:
    if (
        letter.lower() == "a"
        or letter.lower() == "e"
        or letter.lower() == "i"
        or letter.lower() == "o"
        or letter.lower() == "u"
    ):
        phrase = phrase.replace(letter, "")

print(f"Output: {phrase}")
