import re
from prompt_toolkit import prompt
from os import mkdir
from PIL import Image
from prompt_toolkit.completion import NestedCompleter, PathCompleter
import os

def f(path, d):
    d[path] = None
    if os.path.isdir(path):
        for name in os.listdir(path):
            d = f(os.path.join(path, name), d)
    return d


# completer = NestedCompleter.from_nested_dict(f('.', {}))
completer = PathCompleter()

path_to_sheet = prompt(
    "Enter the path to the sprite sheet: ", completer=completer)
width = int(input("How wide is each frame of the sheet? "))
height = int(input("What is the height of each frame of the sheet? "))
rows = int(input("How many rows are in the sheet? "))
cols = int(input("How many columns are in the sheet? "))

folder = path_to_sheet[:-4]
try:
    mkdir(folder)
    print("Created folder:", folder)
except:
    print("Found existing folder:", folder)

sheet = Image.open(path_to_sheet)
count = 1
for y in range(rows):
    for x in range(cols):
        a = (x + 1) * width
        b = (y + 1) * height
        icon = sheet.crop((a - width, b - height, a, b))
        icon.save("{0}/{1}{2}.png".format(folder,
                                          re.split('\\\\|/', folder)[-1], count))
        count += 1
