from PIL import Image, ImageChops, UnidentifiedImageError
import sys

usage = "Usage: image_to_ascii.py input_file output_file [-i]\n\t-i: Invert image colour. Useful when output is displayed using a light font on a dark background."
gradient = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Check command-line arguments
args = sys.argv
argsNum = len(args)

if(argsNum == 1):
    print(f"\n{usage}\n")
    quit()

if(argsNum == 2 or argsNum > 4):
    print(f"\nInvalid number of arguments\n\n{usage}\n")
    quit()

inputPath = args[1]
outputPath = args[2]
invert = False
if(argsNum == 4):
    if(args[3] != "-i"):
        print(f"\nInvalid argument: {args[3]}\n\n{usage}\n")
        quit()
    else:
        invert = True

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