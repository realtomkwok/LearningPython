import os
import shutil

def sortFiles():
    path = os.getcwd()
    os.makedirs("sorted_files/animals", exist_ok=True)
    os.makedirs("sorted_files/plants", exist_ok=True)
    for root, dirs, files in os.walk(path):
        for name in files:
            filePath = os.path.join(root, name)
            if name.endswith(".animal"):
                shutil.copy(filePath, "sorted_files/animals")
            if name.endswith(".plant"):
                shutil.copy(filePath, "sorted_files/plants")

sortFiles()

def categorizeFile(folder):
    for root, dirs, files in os.walk(folder):
         for name in files:
            file = os.path.join(root, name)
            category = open(file).read()
            dst = os.path.join(folder, category)
            os.makedirs(dst, exist_ok=True)
            shutil.move(file, dst)
        
categorizeFile("sorted_files/animals")
categorizeFile("sorted_files/plants")

