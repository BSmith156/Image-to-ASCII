from PIL import Image, ImageChops, UnidentifiedImageError
import sys

usage = "Usage: image_to_ascii.py input_file output_file [-i] [-max n]\n\t-i: Invert image colour. Useful when output is displayed using a light font on a dark background.\n\t-max n: Maximum width/height of output, 0 for no maximum (default 100)."
gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Check command-line arguments
args = sys.argv
argsNum = len(args)

if(argsNum == 1):
    print(f"\n{usage}\n")
    quit()

if(argsNum == 2 or argsNum > 6):
    print(f"\nInvalid number of arguments\n\n{usage}\n")
    quit()

inputPath = args[1]
outputPath = args[2]

# Optional arguments
invert = False
maxSet = False
maxSize = 100

i = 3
while(i < argsNum):
    arg = args[i]
    if(arg == "-i" and not invert):
        invert = True
        i += 1
        continue
    if(arg == "-max" and i != argsNum - 1):
        arg += " " + args[i + 1]
        if(not maxSet and args[i + 1].isnumeric()):
            maxSet = True
            maxSize = int(args[i + 1])
            i += 2
            continue
    print(f"\nInvalid argument: {arg}\n\n{usage}\n")
    quit()

# Open input file
try:
    image = Image.open(inputPath)
except (FileNotFoundError, UnidentifiedImageError) as e:
    print(f"\nInvalid input file: {inputPath}\n\n{usage}\n")
    quit()

# Open output file
try:
    outputFile = open(outputPath, "w")
except FileNotFoundError as e:
    print(f"\nInvalid output file: {outputPath}\n\n{usage}\n")
    quit()

# Resize
if(maxSize > 0):
    image.thumbnail((maxSize, maxSize))

# Convert to greyscale and invert if needed
image = image.convert("L")
if invert:
    image = ImageChops.invert(image)

# Generate output
output = ""
width, height = image.size
for y in range(height):
    for x in range(width):
        colour = image.getpixel((x, y))
        output += gradient[round((colour / 255) * (len(gradient) - 1))]
    output += "\n"
outputFile.write(output)

image.close()
outputFile.close()