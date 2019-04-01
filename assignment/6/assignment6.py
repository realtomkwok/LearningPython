import os
import chardet

def readDecodedFile(filename):
    bytes = min(32, os.path.getsize(filename))
    raw = open(filename, 'rb').read(bytes)
    result = chardet.detect(raw)
    encoding = result['encoding']
     
    infile = open(filename, "r", encoding=encoding)
    data = infile.read()
    infile.close()
     
    print(data)



for root, dir, files in os.walk("salary"):
    for name in files:
        file = open(os.path.join(root, name))
        content = readDecodedFile(file)
        print(content)
        