import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

path = sys.argv[1].strip()

if not path.endswith(".py"):
    sys.exit("Wrong file format")

line_count = 0
try:
    with open(path) as file:
        for line in file:
            if not line.strip(" ").startswith("#") and not line.strip(" ")=="\n":
                line_count+=1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)