def main():
    phrase = shorten(input("Input: ").strip())
    print(f"Output: {phrase}")


def shorten(word):
    for letter in word:
        if (
            letter.lower() == "a"
            or letter.lower() == "e"
            or letter.lower() == "i"
            or letter.lower() == "o"
            or letter.lower() == "u"
        ):
            word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()