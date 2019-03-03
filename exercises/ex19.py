def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"you have {cheeseCount} cheeses!")
    print(f"you have {boxesOfCrackers} boxes of crackers!")
    print("man thats enough for a party!")
    print("get a blanket. \n")

print("we can just give the function numbers directly:")
cheeseAndCrackers(20,30)

print("or, we can use variables from our script:")
amountOfCheese = 10
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers)

print("we can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000)

print("can we ask the user to input the amount?")
cheeseAndCrackers(int(input("how many cheese do ya have: ")), int(input("how many crackers do ya hv: ")))