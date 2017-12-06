import os

os.chdir("/Users/jesentanadi/Desktop/imagetest/hi-res")


for item in os.listdir(os.getcwd()):
    if item != ".DS":
        fName, fExt = os.path.splitext(item)
        gNum, miscInfo = fName.split("_")
        os.rename(item, gNum+fExt)
    