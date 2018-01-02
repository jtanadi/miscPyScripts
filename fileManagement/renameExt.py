"""
Use to rename extensions for uniformity in a dir. Doesn't reformat file to new file type.
"""

import os

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Images/HIGH RESOLUTION IMAGES/NEW HIGH RES/New Folder With Items/new TIFF")

for f in os.listdir(os.getcwd()):
    if f != ".DS_Store":
        fileName, fileExt = os.path.splitext(f)
        newExt = ".tiff"

        newName = fileName + newExt

        os.rename(f, newName)
