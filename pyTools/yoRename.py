import os

y = os.listdir()

for x in y :
    if x[-2:] != "py" and x[-3:] == "pdf" and x[3:] != "HEL" :
        oldName = x
        newName = x[3:]
        print(oldName," || ",newName)
        os.rename(oldName,newName)

