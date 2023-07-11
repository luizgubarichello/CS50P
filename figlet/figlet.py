import sys, getopt
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

try:
    cline = sys.argv
    opts, args = getopt.getopt(cline[1:],"f:","font=")
    if bool(args):
        sys.exit("Invalid usage")
    elif bool(opts):
        for _, font in opts:
            if font in fonts:
                figlet.setFont(font=font)
            else:
                sys.exit("Invalid usage")
    else:
        figlet.setFont(font=random.choice(fonts))
except getopt.GetoptError:
    sys.exit("Invalid usage")
else:
    phrase = input("Input: ")
    print(f"Output:\n{figlet.renderText(phrase)}")
