def main():
    time = input("What time is it? ").strip()
    ctime = 0.0
    if time.endswith("a.m."):
        ctime = convert(time.removesuffix("a.m.").strip())
        if ctime >= 7 and ctime <= 8:
            print("breakfast time")
    elif time.endswith("p.m."):
        ctime = convert(time.removesuffix("p.m.").strip())
        if ctime >= 12 or ctime == 1:
            print("lunch time")
        if ctime >= 6 and ctime <= 7:
            print("dinner time")
    else:
        ctime = convert(time)
        if ctime >= 7 and ctime <= 8:
            print("breakfast time")
        if ctime >= 12 and ctime <= 13:
            print("lunch time")
        if ctime >= 18 and ctime <= 19:
            print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    return float(hour) + (float(minute)/60)


if __name__ == "__main__":
    main()