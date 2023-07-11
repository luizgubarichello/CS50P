import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

path_before = sys.argv[1].strip()
path_after = sys.argv[2].strip()

_, ext_before = splitext(path_before)
_, ext_after = splitext(path_after)
if ext_before != ext_after:
    sys.exit("Input and Output with different extensions")

valid_extensions = [".jpg",".jpeg",".png"]

if ext_before not in valid_extensions or ext_after not in valid_extensions:
    sys.exit("Wrong file format")

try:
    image = Image.open(path_before)
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    image = ImageOps.fit(image, size=shirt_size)
    image.paste(shirt, shirt)
    image.save(path_after)

except FileNotFoundError:
    sys.exit(f"File {path_before} does not exist")
