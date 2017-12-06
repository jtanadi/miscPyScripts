import os

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays/z-JT/")

with open("_TL_NC.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "") : \
               inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
               for i in range(len(codeIndex)-1)}

def makeFolderName(fileName):
    gallery, exhibit, story = fileName.split("_")

    if gallery == "TL":
        if any(n in story for n in ["pt", "st", "ti"]):
            return "{}/{}_{}/01-National Chronology".format(gallery, gallery, exhibit)

        elif "tt" in story:
            return "{}/{}_{}/02-Veterans Stories".format(gallery, gallery, exhibit)

        elif "dl" in story:
            return "{}/{}_{}/03-Dateline".format(gallery, gallery, exhibit)

    return "{}/{}_{}".format(gallery, gallery, exhibit)


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


for key in contentDict:
    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    filePath = os.path.join(pathName, key + ".txt")

    with open(filePath, "w") as writeFile:
        for item in contentDict[key]:
            writeFile.write(item)
