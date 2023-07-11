import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(
            r"^(0?[0-9]|1[0-2])\:?([0-5][0-9])? (AM|PM) to (0?[0-9]|1[0-2])\:?([0-5][0-9])? (AM|PM)$",
            s.strip(),
        )

        inicial_hour = int(matches.group(1))
        inicial_minute = matches.group(2)
        inicial_id = matches.group(3)
        final_hour = int(matches.group(4))
        final_minute = matches.group(5)
        final_id = matches.group(6)

        if inicial_id == "PM" and inicial_hour != 12:
            inicial_hour = inicial_hour + 12
        elif inicial_id == "AM" and inicial_hour == 12:
            inicial_hour = 0
        if final_id == "PM" and final_hour!=12:
            final_hour = final_hour + 12
        elif final_id == "AM" and final_hour == 12:
            final_hour = 0

        if inicial_minute == None:
            inicial_minute = 00
        else:
            inicial_minute = int(matches.group(2))
        if final_minute == None:
            final_minute = 00
        else:
            final_minute = int(matches.group(5))

        return f"{inicial_hour:02}:{inicial_minute:02} to {final_hour:02}:{final_minute:02}"

    except AttributeError:
        raise ValueError("Invalid Time / Format")


if __name__ == "__main__":
    main()
