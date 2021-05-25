import sys

usage = "Usage: image_to_ascii.py input_file output_file [-i]\n\t-i: Invert output colour. Useful when output is displayed using a light font and dark background."

# Check command-line arguments
args = sys.argv
argsNum = len(args)

if(argsNum == 1):
    print(f"\n{usage}\n")
    quit()

if(argsNum == 2 or argsNum > 4):
    print(f"\nInvalid number of arguments\n\n{usage}\n")
    quit()

invert = False
if(argsNum == 4):
    if(args[3] != "-i"):
        print(f"\nInvalid argument: {args[3]}\n\n{usage}\n")
        quit()
    else:
        invert = True