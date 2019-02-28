from sys import argv

script, fileName = argv

print(f"we're going to erase {fileName}")
print("if you don't want that, hit CTRL-C")
print("if you do want that, hit RETURN")

input("?")

print("opening the file...")
target = open(fileName, 'w')

print("truncating the file. goodbye!")
target.truncate

print("now im going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("im going to write these to the file.")

target.write(f'{line1} \n{line2} \n{line3} \n')

print("And finally, we close it.")
target.close()