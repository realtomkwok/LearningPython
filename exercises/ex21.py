def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def multifply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"divding {a} / {b}")
    return a / b

print("let's do some math w just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multifply(90, 2)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# a puzzle for the extra credit, type it in anyway,
print("here is a puzzle.")

what = add(age, subtract(height, multifply(weight, divide(iq, 2))))

print("that becomes:", what, "can you do it by hand?")