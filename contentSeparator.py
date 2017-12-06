import os

os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays/z-JT/TL")

with open("_TL_VS.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", ""): inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
               for i in range(len(codeIndex)-1)}

def makeFolderName(fileName):
    if any(n in fileName for n in ["pt", "st", "ti"]):
        return os.path.join("01-National Chronology", fileName[:7])

    if "tt" in fileName:
        return os.path.join("02-Veterans Stories", fileName[:7])

    if "dl" in fileName:
        return os.path.join("03-Dateline", fileName[:7])

    return fileName[:7]

def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


for key in contentDict:
    folderName = makeFolderName(key)
    makeFolder(folderName)

    filePath = os.path.join(folderName, key + ".txt")

    with open(filePath, "w") as writeFile:
        writeFile.write(contentDict[key])

    # sys.stdout = open(filePath, 'w+')

    # for item in contentDict[key]:
    #     print item
