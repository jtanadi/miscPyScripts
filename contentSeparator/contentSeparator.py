import os

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays/z-JT")

with open("_TH.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] : \
               inputTextList[codeIndex[i]+1:codeIndex[i+1]] \
               for i in range(len(codeIndex)-1)}

def makeFolderName(fileName):
    exhibit, topic, story = fileName.split("_")

    # if exhibit == "TH":
    #     if "ip" in story:
    #         category = "0-Intro"

    #     elif "pt" in story:
    #         category = "1-Primary"

    #     elif "st" in story:
    #         category = "2-Secondary"

    return "{}/".format(exhibit)

    """
    Fix TL version below once folder structure has been decided.
    """
    # if gallery == "TL":
    #     if any(n in story for n in ["pt", "st", "ti"]):
    #         return "{}/{}_{}/01-National Chronology".format(gallery, gallery, exhibit)

    #     elif "tt" in story:
    #         return "{}/{}_{}/02-Veterans Stories".format(gallery, gallery, exhibit)

    #     elif "dl" in story:
    #         return "{}/{}_{}/03-Dateline".format(gallery, gallery, exhibit)


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


for key in contentDict:

    title = contentDict[key][0].replace("\n", "")
    body = contentDict[key][1:]

    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    titlePath = os.path.join(pathName, key.upper() + "-T.txt")
    bodyPath = os.path.join(pathName, key.upper() + "-B.txt")

    with open(titlePath, "w") as writeTitleFile:
        for item in title:
            writeTitleFile.write(item)

    with open(bodyPath, "w") as writeBodyFile:
        for item in body:
            writeBodyFile.write(item)
