months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip().title()

    if "/" in date:
        month, day, year = date.split("/")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            continue
        if day > 31 or month > 12:
            continue

    else:
        try:
            monthw, day, year = date.split(" ")
            if "," in day:
                day = day.removesuffix(",")
            else:
                continue
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if int(day) > 31 or monthw not in months:
            continue
        for cont in range(len(months)):
            if monthw == months[cont]:
                month = cont+1

    print("{year}-{month:02}-{day:02}".format(year = year, month = month, day = day))
    break