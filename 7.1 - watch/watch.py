import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = s.strip()
    matches = re.search(r"^<iframe.*src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\".*</iframe>$", url)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()