import glob
def displayFiles():
    files = glob.glob("/home/shrvnchndra/Documents/ToDo Lists/*.txt")
    count = 1;  print("Available Files are:")
    for file in files:
        print(str(count) + ".\t" + file[39:])
        count += 1
    print('\n')

def selectFile():
    request = input("Select File: ") + '.txt'
    if "create" in request:
        fileName = input("Enter file name:") + '.txt'
        with open(fileName, 'x') as file:
            pass
    return fileName

def getLineNumber(fileName):
    with open(fileName, 'r') as file:
        return len(file.readlines()) + 1
def printList(fileName):
    print("\n" + fileName[:-4])
    with open(fileName, 'r') as file:
        for line in file:
            print(line, end ="")
    print('\n')
def addItem(fileName, item, lineNumber):
    with open(fileName, 'a') as file:
        file.write(str(lineNumber) + '.\t' + item +'\n')
def deleteItem(fileName, item):
    with open(fileName, 'r+') as file:
        contents = file.readlines()
        file.seek(0);   count = 1
        for line in contents:
            if item not in line:
                if count < 10:
                    file.write(str(count) + '.\t' + line[3:])
                else:   file.write(str(count) + '.\t' + line[4:])
                count += 1
        file.truncate()
def deleteLine(fileName, lineNumber):
    with open(fileName, 'r+') as file:
        contents = file.readlines()
        file.seek(0);   count = 1
        for line in contents:
            if lineNumber not in line:
                if count < 10:
                    file.write(str(count) + '.\t' + line[3:])
                else:   file.write(str(count) + '.\t' + line[4:])
                count += 1
        file.truncate()

displayFiles()
fileName = selectFile()
flag = True
while flag:
    lineNumber = getLineNumber(fileName)
    request = input("Enter your Request:")
    if ("print" in request): printList(fileName)
    elif ("delete all" in request): open(fileName, 'w').close()
    elif ("add" in request[:4]): addItem(fileName, request[4:], lineNumber)
    elif ("delete line" in request): deleteLine(fileName, request[12:])
    elif ("delete" in request[:7]): deleteItem(fileName, request[7:])
    else:   flag = False
