import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    umlist = re.findall(r"\bum\b",s.lower(), flags = re.IGNORECASE)
    return len(umlist)


if __name__ == "__main__":
    main()