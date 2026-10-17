# submit50 cs50/problems/2022/python/figlet
from pyfiglet import Figlet
import sys, random

figlet = Figlet()

list_font = figlet.getFonts()

if len(sys.argv) == 1:
    str = input('Input: ')
    f = random.choice(list_font)
    figlet.setFont(font=f)
    print(figlet.renderText(str))
elif len(sys.argv) == 3:
    if (sys.argv[1] in ('-f', '--font')) and (sys.argv[2] in list_font):
        str = input('Input: ')
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(str))
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')


