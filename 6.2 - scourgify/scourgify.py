import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

path_before = sys.argv[1].strip()
path_after = sys.argv[2].strip()

if not path_before.endswith(".csv") or not path_after.endswith(".csv"):
    sys.exit("Wrong file format")

beings  =[]

try:
    with open(path_before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            beings.append({"first": first, "last": last, "house": row["house"]})
    with open(path_after, "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for being in beings:
            writer.writerow(being)

except FileNotFoundError:
    sys.exit(f"File {path_before} does not exist")