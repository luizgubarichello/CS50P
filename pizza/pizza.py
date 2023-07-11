import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

path = sys.argv[1].strip()

if not path.endswith(".csv"):
    sys.exit("Wrong file format")

try:
    with open(path) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")