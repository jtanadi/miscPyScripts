import os
import collections as c

# Remember to change directory
os.chdir("/Volumes/3Projects/OVMM-OhioVetMem/02_CONTENT/Exhibit Script_FINAL/Thematic Displays/")

with open("_THCaptions.txt", 'rU') as readFile: #.txt file
    inputTextList = readFile.readlines() #Returns a list

inputTextList = [text for text in inputTextList if text != "\n"]

codeIndex = [index for index, entry in enumerate(inputTextList) if "_" in entry]
codeIndex.append(len(inputTextList))

contentDict = {inputTextList[codeIndex[i]].replace("\n", "").split(" ")[0] : inputTextList[codeIndex[i]+2:codeIndex[i+1]] for i in range(len(codeIndex)-1)}
contentDict = c.OrderedDict(sorted(contentDict.items()))

def combineCaptions():
    """
    Function to combine different captions across the same exhibit & topic
    """

    exhibitTopic, keyMemory = " ", " "
    newContentDict = {}

    for key in contentDict:
        
        if exhibitTopic in key:
            newContentDict[exhibitTopic] = contentDict[key] + contentDict[keyMemory]

        keyMemory = key

        exhibit, topic, cap = key.split("_")
        exhibitTopic = "{}_{}".format(exhibit, topic)

    return newContentDict


def makeFolderName(fileName):
    """
    Function to make folders based on file name
    Returns a path to be used by makeFolder() function

    Currently a little inconsistent with how it treats exhibits
    """

    exhibit, topic = fileName.split("_")

    if exhibit == "TH":
        return "{}/CAPTION/".format(exhibit)

    elif exhibit == "TL":
        return "{}/{}/".format(exhibit, topic.upper())


def makeFolder(folder):
    if os.path.exists(folder):
        pass
    else:
        os.makedirs(folder)


combinedContent = combineCaptions()

for key in combinedContent:
    pathName = makeFolderName(key)
    makeFolder(str(pathName))

    bodyPath = os.path.join(pathName, key.upper() + ".txt")

    with open(bodyPath, "w") as wBodyFile:
        for item in combinedContent[key]:
            wBodyFile.write(item + "\n")
