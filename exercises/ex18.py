# this one is like your scripts w argv
def printTwo(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#that *args is actually pointless, we can just do this
def printTwoAgain(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def printOne(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def printNone():
    print("i got nothin.")

printTwo("Tom", "Zed")
printTwoAgain("Tom", "Zed")
printOne(input("just type: "))
printNone()