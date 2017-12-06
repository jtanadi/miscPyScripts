myDict = {"TH_ex_01":"Hello how are you", "TH_ex_02":"Buona serra!", "TH_ex03":"Good afternoon!"}

for key in myDict:
    with open(key + ".txt", "w") as f:
        f.write(myDict[key])