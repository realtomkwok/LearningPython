import os
import shutil

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

def cleanFile(content):
    invaildChar = '#-='
    processedContent = ''.join(c for c in content if c not in invaildChar)
    cleanContent, waste = processedContent.split(' █')
    finalContent = cleanContent.replace(': ', '的工资为')
    return(finalContent)

def compile_employee_salaries(path):
    for root, dir, files in os.walk(path):
        for name in files:
            file = os.path.join(root, name)
            content = decode(file)
            cleanContent = cleanFile(content)

            # write 'em into a new file
            with open('salaries.txt', 'a') as targetFile:
                targetFile.write(cleanContent + '\n')

    os.makedirs('output_file', exist_ok=True)
    shutil.move('salaries.txt', 'output_file')

compile_employee_salaries('salary')
print('Your salary sheet is ready. Check the `output_file` folder!')

def sort_employee_salaries(fileName):
    with open(fileName) as f:
        d = {}
        for line in f:
            name, salary =line.split('的工资为')
            number, others = salary.split('元')
            d[name] = int(number) #make a dict
            sortedList = sorted(d.items(), key=lambda x:(-x[1], x[0]))
        with open('output_file/sorted_salaries.txt', 'w') as sortedFile:
            count = 1
            for item in sortedList:
                # output turple into a text file.
                content = '%s %s' % item
                sortedFile.write(str(count) + ' ' + content + '\n')
                count += 1

sort_employee_salaries('output_file/salaries.txt')
print('Your salary sheet is sorted in a descending order. Check the `output_file` folder!')



