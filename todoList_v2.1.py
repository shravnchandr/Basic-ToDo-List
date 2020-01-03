import glob
import os

def displayFiles():
    files = glob.glob("/home/shrvnchndra/Documents/My Projects/ToDo Lists/*.txt")
    count = 1;  print("Available Files are:")
    for file in files:
        print(str(count) + ".\t" + file[51:])
        count += 1
    print('\n')
def selectFile():
    request = input("Select File: ") + '.txt'
    if "create" in request:
        fileName = input("Enter file name:") + '.txt'
        with open(fileName, 'x') as file:
            pass
        return fileName
    return request
def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    else:   print("The File does not Exist")

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

displayFiles()
fileName = selectFile()
flag = True
while flag:
    lineNumber = getLineNumber(fileName)
    request = input("Enter your Request:")
    if ("print" in request): printList(fileName)
    elif ("delete all" in request): open(fileName, 'w').close()
    elif ("delete file" in request):    deleteFile(fileName);   flag = False
    elif ("add" in request[:4]): addItem(fileName, request[4:], lineNumber)
    elif ("delete" in request[:7]): deleteItem(fileName, request[7:])
    else:   flag = False
