"""
Use to rename extensions for uniformity in a dir. Doesn't reformat file to new file type.
"""

import os

# Remember to change directory
os.chdir("/Users/jesentanadi/Desktop/Ohio Test/Image/-")

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)
        newExt = ".tiff"

        newName = fileName + newExt

        os.rename(f, newName)
