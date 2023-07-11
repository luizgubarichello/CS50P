def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    numerator, denominator = fraction.strip().split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    if numerator > denominator:
        raise ValueError("X can't be greater than Y")
    return round(100 * (int(numerator) / int(denominator)))


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()