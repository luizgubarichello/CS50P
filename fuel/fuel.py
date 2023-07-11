while True:
    try:
        numerator, denominator = input("Fraction: ").strip().split("/")
        tank = round(100 * (int(numerator) / int(denominator)))
    except (ValueError, ZeroDivisionError):
        continue
    else:
        if int(numerator)>int(denominator):
            continue
        if tank<=1:
            print("E")
            break
        elif tank>=99:
            print("F")
            break
        else:
            print(f"{tank}%")
            break