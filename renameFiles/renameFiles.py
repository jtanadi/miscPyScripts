import os

os.chdir("/Users/jesen/Desktop/tester")

for f in os.listdir(os.getcwd()):
    fileName, fileExt = os.path.splitext(f)

    title, course, num = fileName.split("-")

    title = title.strip()
    course = course.strip()
    num = num.strip()[1:].zfill(2)

    newName = "{}-{}{}".format(num, title, fileExt)

    os.rename(f, newName)