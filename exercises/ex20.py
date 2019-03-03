from sys import argv

script, inputFile = argv

def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printALine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

print("first lets print the whole file: \n")
printAll(currentFile)

print("now lets rewind, kind of like a tape.")
rewind(currentFile)

print("lets print three lines:")

currentLine = 1
printALine(currentLine, currentFile)

currentLine = currentLine + 1
printALine(currentLine,currentFile)

currentLine = currentLine +1
printALine(currentLine,currentFile)