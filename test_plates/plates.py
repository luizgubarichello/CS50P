def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<3 or len(s)>6:
        return False
    for letter in s[:2]:
        if letter.isnumeric():
            return False
    for letter in s:
        if letter.isalnum() == False:
            return False
    for i in range(len(s)):
        if i>1 and i<len(s):
            if s[i:].isnumeric() and not s[i:].startswith("0"):
                return True
            elif s[i:].isalpha():
                return True
            else:
                if s[i:].isalnum() and not s[i:].isalpha() and not s[i:i+1].isnumeric():
                    continue
                return False


if __name__ == "__main__":
    main()