import os
import re
from PIL import Image
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from os import mkdir

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
for r in range(rows):
    for c in range(cols):
        x = (c + 1) * width
        y = (r + 1) * height
        icon = sheet.crop((x - width, y - height, x, y))
        icon.save("{0}/{1}{2}.png".format(folder,
                                          re.split('\\\\|/', folder)[-1], count))
        count += 1
