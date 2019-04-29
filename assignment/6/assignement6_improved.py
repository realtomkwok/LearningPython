import os
import shutil
import re

def decode(fileName):
    encoding = ['utf-8', 'GBK', 'big5']
    for e in encoding:
        try:
            file = open(fileName, 'r', encoding=e)
            content = file.read()
        except UnicodeDecodeError:
            continue
        else:
            return(content)

for root, dir, files in os.walk('salary'):
        for name in files:
            file = os.path.join(root, name)
            content = re.search(r'\w+: \d*', decode(file))
            with open('salaries.txt', 'a') as targetFile:
                # print Match objects from re.search
                if content:
                    targetFile.write(content.group(0)+'\n')