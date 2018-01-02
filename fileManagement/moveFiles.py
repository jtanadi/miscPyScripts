"""
Use to rename parsed script files in Combat 1 & Combat 2 to match panel codes
"""

import os

# Remember to change directory
os.chdir("/Users/jesentanadi/Desktop/Ohio Test/Image")

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)

        if fileExt == ".tiff" or fileExt == ".tif":
            oldPath = os.path.join(os.getcwd(), f)
            newPath = os.path.join("/Users/jesentanadi/Desktop/Ohio Test/Image/-", f)

            os.rename(oldPath, newPath)
