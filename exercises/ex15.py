from sys import argv
#import argv

script, filename = argv
#define two variables from argv

txt = open(filename)
#let txt open the exact file w the filename

print(f"here's your file {filename}")
print(txt.read())
#print the sample text

print("Type the filename again:")
fileAgain = input("> ")
#do the same shit again

txtAgain = open(fileAgain)

print(txtAgain.read())