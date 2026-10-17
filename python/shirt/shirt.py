# submit50 cs50/problems/2022/python/shirt
from PIL import Image, ImageOps
import sys, os

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        if os.path.splitext(sys.argv[1])[1].lower() not in ('.jpg', '.jpeg', '.png'):
            sys.exit('Invalid input')
        elif os.path.splitext(sys.argv[2])[1].lower() not in ('.jpg', '.jpeg', '.png'):
            sys.exit('Invalid output')
        elif os.path.splitext(sys.argv[1])[1] !=  os.path.splitext(sys.argv[2])[1]:
            sys.exit('Input and output have different extensions')
        else:
            try:
                shirt = Image.open('shirt.png')
                size = shirt.size
                img = Image.open(sys.argv[1])

                img = ImageOps.fit(img, size)

                img.paste(shirt, shirt)
                img.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit('Input does not exist')

main()
