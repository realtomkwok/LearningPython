import os
import re

with open('complete-crew.txt') as file:
    content = re.findall(r'(\'|\")(.{0,20})\1 (\(\d+\))\s+(|{.+})	(.+)', file.read())
    with open('test.txt', 'a') as targetFile:
        for group in content:
            print('{} {} {} {} \n'.format(group[1], group[2], group[3], group[4]))