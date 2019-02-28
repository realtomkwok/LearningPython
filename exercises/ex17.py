from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"copying from {fromFile} to {toFile}")

#we could do these two on one line, how?
inFile = open(fromFile)
inData = inFile.read()

print(f"the input file is {len(inData)} bytes long")

print(f"does the output file exist? {exists(toFile)}")
print("ready, hit RETURN to continue, CTRL-C to abort.")
input()

outFile = open(toFile, 'w')
outFile.write(inData)

print("ight, all done.")

outFile.close()
inFile.close()